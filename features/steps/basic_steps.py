import datetime
import random
import string
import time
import telebot

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

import pages


@step('click on {element_name}')
def step_impl(context, element_name):
    context.current_page.click_on(element_name)


@step('type "{text}" in {field_name}')
def step_impl(context, text, field_name):
    if text == 'random':
        text = f"{random_char(7)}@{random_char(7)}.com"
    context.current_page.type_in(field_name, text)


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


@step('see "{text}" in {element}')
def step_impl(context, text, element):
    element_text = context.current_page.get_text(element)
    if text not in element_text:
        raise RuntimeError(f'Текст элемента "{element}": {element_text}. Ожидаемый текст: {text}')


@step('see "{text}" on the page')
def step_impl(context, text):
    element = (By.TAG_NAME, 'body')
    WebDriverWait(context.driver, 5).until(
        ec.text_to_be_present_in_element(element, text), f'"{text}" текст не найден на странце')


@then('I am on {page_name} page')
def init_screen(context, page_name):
    """Instantiating verifies that we're on that page"""
    page_class = pages.factory(page_name)
    context.current_page = page_class(context.driver)


@step('open url: "{url}"')
def step_impl(context, url):
    context.driver.get(url)


@step('жду "{seconds}" сек')
def step_impl(context, seconds):
    time.sleep(int(seconds))


@when("scroll down")
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


@step("print pagesource")
def step_impl(context):
    print(context.driver.page_source)


@step("обнулить таймер")
def step_impl(context):
    context.time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)


@step('считаю время загрузки "{name}"')
def step_impl(context, name):
    time_diff = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3) - context.time
    context.time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
    if name == 'cart':
        context.cart = float(time_diff.total_seconds())
    elif name == 'home':
        context.home = float(time_diff.total_seconds())
    # elif name == 'payment_before':
    #     context.payment_before = float(time_diff.total_seconds())
    # elif name == 'payment_after':
    #     context.payment_after = float(time_diff.total_seconds())
    else:
        context.payment = float(time_diff.total_seconds())


@step("отсылаю результат в гугл таблицу")
def step_impl(context):
    cart = float(context.cart) if context.cart else 0
    page = float(context.home) + cart
    context.data_worksheet.insert_rows(
        values=[[context.time.strftime('%Y-%m-%d %H:%M:%S'),
                 float(context.home),
                 cart,
                 context.landing,
                 page]], row=2)


@then("проверяю наличие элемента {element_name}")
def step_impl(context, element_name):
    if element_name != '3d secure widget':
        context.current_page.get_element(element_name, timeout=50)
    else:
        for i in range(50):
            try:
                context.current_page.get_element(element_name, timeout=1)
                break
            except (TimeoutException, WebDriverException):
                try:
                    context.driver.switch_to.frame(context.driver.find_element_by_tag_name('iframe'))
                except NoSuchElementException:
                    pass
        else:
            print(4)
            raise RuntimeError(f'"{element_name}" не найден')


@step('отправляю скриншот в чат "{chat_id}" для страницы "{page}" с разрешением "{resolution}"')
def step_impl(context, chat_id, page, resolution):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    width = resolution.split('x')[0]
    height = resolution.split('x')[1]
    driver.set_window_size(width, height)
    url = context.config.get('websites', page)
    driver.get(url)
    time.sleep(30)
    bot = telebot.TeleBot("1461082086:AAGUnZJyEcDwkW1LPHLmezbrXEDzIu6nD8k")
    date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=3)
    s_date = date.strftime('%d-%b %H:%M')
    screen = driver.get_screenshot_as_png()
    bot.send_photo(chat_id=int(chat_id), photo=screen, caption=f'Отчет {str(s_date)}')
    driver.quit()
