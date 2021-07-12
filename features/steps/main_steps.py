import random
import string
import time
from datetime import datetime, timezone, timedelta

from behave import *
from selenium.common.exceptions import StaleElementReferenceException

import pages
import steps
from pages import MainPage


@step('открываю {page_name} страницу')
def step_impl(context, page_name):
    if page_name.startswith(('http', 'www')):
        url = page_name
    else:
        url = context.config.get('websites', page_name)
    context.landing = page_name
    context.driver.get(url)
    context.current_page = MainPage(context.driver)


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


@when("перехожу на страницу {page_name}")
def step_impl(context, page_name):
    if page_name == 'cart':
        context.current_page.scroll_to('activate button')
        context.current_page.click_on('activate button')
        context.current_page.click_on('email field')
        context.current_page.type_in('email field', f"{random_char(7)}@{random_char(7)}.com")
        context.time = datetime.now(timezone.utc) + timedelta(hours=3)
        context.current_page.click_on('next button')
    elif page_name in ('alfabank', 'cloudpayments'):
        try:
            context.current_page.click_on('confirm checkbox', timeout=20)
        except StaleElementReferenceException:
            time.sleep(2)
            context.current_page.click_on('confirm checkbox', timeout=5)
        context.time = datetime.now(timezone.utc) + timedelta(hours=3)
        context.current_page.click_on('continue button')
    page_class = pages.factory(page_name)
    context.current_page = page_class(context.driver)
