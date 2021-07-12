import gspread
from google.oauth2.service_account import Credentials


class GoogleSheets:
    data_columns = {
        'Date': 'A',
        'Page': 'B',
        'Loading': 'C'
    }

    def authorize(self, work_sheet):
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_file("features/fitness-automation-299213-675b2746599f.json", scopes=scope)
        gs = gspread.authorize(creds).open_by_key("12-P5XcVUfZ-jeSKt8btAgNNc7tEbf7oOJIqPA_9gwI4")
        return gs.worksheet(work_sheet)
