import datetime
import random
import time

from behave import *


@step('ввожу карту {card_type}')
def enter_details(context, card_type):
    month = random.randint(1, 9)
    if month < 10:
        month = f'0{month}'
    year = random.randint(22, 23)
    cvc = random.randint(100, 300)
    if card_type == 'fake card':
        context.current_page.type_in('cardnumber field', '5555555555554444')
        context.current_page.type_in('month field', f'{month}')
        context.current_page.type_in('year field', f'{year}')
        context.current_page.type_in('cardholder field', 'USERNAME USERNAME')
        context.current_page.type_in('cvc field', f'{cvc}')
        context.time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
        context.current_page.click_on('pay button')
    elif card_type == 'real card':
        context.current_page.type_in('cardnumber field', '4214870006156277')
        context.current_page.type_in('month field', f'{month}')
        context.current_page.type_in('year field', f'{year}')
        context.current_page.type_in('cardholder field', 'USERNAME USERNAME')
        context.current_page.type_in('cvc field', f'{cvc}')
        context.time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
        context.current_page.click_on('pay button')
    elif card_type == 'alfa card':
        context.current_page.type_in('cardnumber field', '4214870006156277')
        context.current_page.type_in('cardholder field', 'USERNAME USERNAME')
        context.current_page.type_in('expired field', f'{month}{year}')
        context.current_page.type_in('cvc field', str(cvc))
        time.sleep(0.5)
        context.current_page.click_on('pay button')
    context.time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
    try:
        context.current_page.get_element('exired error',timeout=2)
        context.current_page.type_in('cvc field', str(random.randint(100, 300)))
        context.current_page.click_on('pay button')
        context.time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
    except:
        pass

