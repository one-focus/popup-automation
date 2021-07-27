from datetime import datetime
from time import sleep

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import gmail
import pages

use_step_matcher('re')


@when('click on (?P<element_name>[^"]*?)(?: in "(?P<section>[^"]*?)")?')
def click_on(context, element_name, section=None):
    if section:
        section_xpath = context.current_page.get_element_by_name(section)[1]
        element = context.current_page.get_element_by_name(element_name)
        if element[0] == 'xpath':
            try:
                context.driver.find_element_by_xpath(f'{section_xpath}{element[1]}').click()
            except NoSuchElementException:
                raise RuntimeError(f'Не могу кликнуть {element_name} в {section}')
        else:
            raise RuntimeError(f'Используй XPATH для локатора {element_name}')
    else:
        context.current_page.click_on(element_name)


@when('enter "(?P<text>[^"]*)" in (?P<field_name>[^"]*)(?: in "(?P<section>[^"]*?)")?')
def enter_in(context, text, field_name, section=None):
    if 'generated' in text:
        context.values[text] = text = text.replace("generated", f'{datetime.now().strftime("%d.%m.%Y %H:%M:%S")}')
    if section:
        section_xpath = context.current_page.get_element_by_name(section)[1]
        element = context.current_page.get_element_by_name(field_name)
        if element[0] == 'xpath':
            try:
                context.driver.find_element_by_xpath(f'{section_xpath}{element[1]}').send_keys(text)
            except NoSuchElementException:
                raise RuntimeError(f'Не могу найти {field_name} в {section}')
        else:
            raise RuntimeError(f'Используй XPATH для локатора {field_name}')
    else:
        context.current_page.type_in(field_name, text)


@then('text "(?P<text>.*)" in (?P<element>.*) is displayed')
def text_in_element_is_state(context, text, element):
    element_text = context.current_page.get_text(element)
    if text not in element_text:
        raise RuntimeError(f'{element} text is {element_text}. Expected: {text}')


@then('text "(?P<text>.*)" is displayed')
def text_is_state(context, text):
    element = (By.TAG_NAME, 'body')
    WebDriverWait(context.driver, 5).until(
        ec.text_to_be_present_in_element(element, text), f'Unable to find text: {text}')


@step('page (?P<page_name>.*) is opened')
def init_screen(context, page_name):
    """Instantiating verifies that we're on that page"""
    page_class = pages.factory(page_name)
    context.current_page = page_class(context.driver)


@step('open url: "(?P<url>.*)"')
def open_url(context, url):
    context.driver.get(url) if url.startswith('http') else context.driver.get(f'https://{url}')


@given('open (?P<page_name>.*) page')
def open_page(context, page_name):
    open_url(context, page_name)
    page_class = pages.factory(page_name)
    context.current_page = page_class(context.driver)


@when('remember (?P<key>.*) as "(?P<value>.*)"')
def remember(context, key, value):
    context.values[value] = context.current_page.get_text(key)


@then('email with "(?P<query>.*)" contains "(?P<text>.*)"')
def step_impl(context, query, text):
    query = replace_with_context_values(context, query)
    text = replace_with_context_values(context, text)
    for i in range(20):
        messages = gmail.search_message(query)
        if len(messages) < 1:
            sleep(6)
        elif len(messages) == 1:
            message = messages[0].replace('\r\n', ' ').replace('\xa0', ' ')
            break
        else:
            RuntimeError(f'Для "{query}" найдено сообщений: {len(messages)}. Должно быть 1. Измените параметр поиска')
    else:
        raise RuntimeError(f'Сообщение с текстом {query} не пришло на почту в течение 1 минуты')

    errors = []
    for search_text in text.split(';'):
        if search_text not in message:
            errors.append(f'"{search_text}" not found in "{message}"')
    if errors:
        raise RuntimeError(errors)


def replace_with_context_values(context, text):
    for value in context.values:
        if value in text:
            text = text.replace(value, context.values[value])
    return text


@when("wait (?P<seconds>.*) sec")
def step_impl(context, seconds):
    sleep(int(seconds))
