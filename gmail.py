import os.path
from google.oauth2.credentials import Credentials
from apiclient import errors
import email
from email.mime.text import MIMEText
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://mail.google.com/']


def search_message(search_string):
    """
    Search the inbox for emails using standard gmail search parameters
    and return a list of email IDs for each result
    PARAMS:
        service: the google api service object already instantiated
        user_id: user id for google api service ('me' works here if
        already authenticated)
        search_string: search operators you can use with Gmail
        (see https://support.google.com/mail/answer/7190?hl=en for a list)
    RETURNS:
        List containing email IDs of search query
    """
    service = get_service()
    try:
        # initiate the list for returning
        list_messages = []

        # get the id of all messages that are in the search string
        search_ids = service.users().messages().list(userId='me', q=search_string).execute()

        # if there were no results, print warning and return empty string
        try:
            ids = search_ids['messages']

        except KeyError:
            # print("WARNING: the search queried returned 0 results")
            # print("returning an empty string")
            return ""

        if len(ids) > 1:
            for msg_id in ids:
                list_messages.append(get_message(service, 'me', msg_id['id']))
            return (list_messages)

        else:
            list_messages.append(get_message(service, 'me', ids[0]['id']))
            return list_messages

    except errors.HttpError as error:
        print(f"An error occured: {error}")


def get_message(service, user_id, msg_id):
    """
    Search the inbox for specific message by ID and return it back as a
    clean string. String may contain Python escape characters for newline
    and return line.

    PARAMS
        service: the google api service object already instantiated
        user_id: user id for google api service ('me' works here if
        already authenticated)
        msg_id: the unique id of the email you need
    RETURNS
        A string of encoded text containing the message body
    """
    try:
        # grab the message instance
        message = service.users().messages().get(userId=user_id, id=msg_id, format='raw').execute()

        # decode the raw string, ASCII works pretty well here
        msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

        # grab the string from the byte object
        mime_msg = email.message_from_bytes(msg_str)

        # check if the content is multipart (it usually is)
        content_type = mime_msg.get_content_maintype()
        if content_type == 'multipart':
            # there will usually be 2 parts the first will be the body in text
            # the second will be the text in html
            parts = mime_msg.get_payload()

            # return the encoded text
            final_content = parts[0].get_payload()
            return final_content

        elif content_type == 'text':
            return mime_msg.get_payload()

        else:
            # print("\nMessage is not text or multipart, returned an empty string")
            return ""
    # unsure why the usual exception doesn't work in this case, but
    # having a standard Exception seems to do the trick
    except Exception as error:
        print(f"An error occured: {error}")


def get_service():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)


def delete_all_emails():
    service = get_service()
    search_ids = service.users().messages().list(userId='me').execute()
    if 'messages' in search_ids:
        [service.users().messages().trash(userId='me', id=id['id']).execute() for id in search_ids['messages']]


if __name__ == '__main__':
    delete_all_emails()
