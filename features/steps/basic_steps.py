from datetime import datetime, timezone, timedelta
from time import sleep

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import gmail
import pages
import urllib.request

use_step_matcher('re')


@when('click on (?P<element_name>[^"]*?)(?: in "(?P<section>[^"]*?)")?')
def click_on(context, element_name, section=None):
    sleep(0.5)
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
    sleep(0.5)
    if 'generated' in text:
        time = datetime.now(timezone.utc) + timedelta(hours=3)
        context.values[text] = text = text.replace("generated", f'{time.strftime("%d.%m.%Y %H:%M:%S")}')
    if section:
        section_xpath = context.current_page.get_element_by_name(section)[1]
        element = context.current_page.get_element_by_name(field_name)
        if element[0] == 'xpath':
            try:
                element = context.driver.find_element_by_xpath(f'{section_xpath}{element[1]}')
                element.clear()
                element.send_keys(text)
            except NoSuchElementException:
                raise RuntimeError(f'Не могу найти {field_name} в {section}. With xpath {section_xpath}{element[1]}')
        else:
            raise RuntimeError(f'Используй XPATH для локатора {field_name}')
    else:
        context.current_page.type_in(field_name, text)


@then('text "(?P<text>.*)" in (?P<element>.*) is displayed')
def text_in_element_is_state(context, text, element):
    element_text = context.current_page.get_text(element)
    if text not in element_text:
        raise RuntimeError(f'Текст для элемента {element}: "{element_text}". Ожидаемый: {text}')


@then('text "(?P<text>.*)" is displayed')
def text_is_state(context, text):
    element = (By.TAG_NAME, 'body')
    WebDriverWait(context.driver, 10).until(
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
    context.page_name = page_name
    open_url(context, page_name)
    page_class = pages.factory(page_name)
    context.current_page = page_class(context.driver)


@when('remember (?P<key>.*) as "(?P<value>.*)"')
def remember(context, key, value):
    context.values[value] = context.current_page.get_text(key)


@then('email with "(?P<query>.*)" contains "(?P<text>.*)" in (?P<seconds>.*) sec')
def step_impl(context, query, text, seconds):
    query = replace_with_context_values(context, query)
    text = replace_with_context_values(context, text)
    sleep(5)
    for i in range(10):
        messages = gmail.search_message(query)
        if len(messages) < 1:
            sleep(int(seconds) / 10)
        elif len(messages) == 1:
            message = messages[0].replace('\r\n', ' ').replace('\xa0', ' ')
            break
        else:
            RuntimeError(f'Для "{query}" найдено сообщений: {len(messages)}. Должно быть 1. Измените параметр поиска')
    else:
        raise RuntimeError(f'Сообщение с текстом "{query}" не пришло на почту в течение {seconds} секунд')

    errors = []
    for search_text in text.split(';'):
        if search_text not in message:
            errors.append(f'"{search_text}" не найден в "{message}"')
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


@when("download cat image")
def step_impl(context):
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.request.urlretrieve(
        "https://cataas.com/cat/says/%D0%BC%D0%BD%D0%B5%20%D0%BD%D1%83%D0%B6%D0%B5%D0%BD%20%D0%B2%D0%B5%D1%81%D1%8C%20%D0%BC%D0%B5%D1%82%D0%B0%D0%BB",
        "cat.jpg")


@when("open last tab")
def step_impl(context):
    context.driver.switch_to_window(context.driver.window_handles[-1])
