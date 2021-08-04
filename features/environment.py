import configparser

from sys import platform
from selenium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
import telebot

# TODO check all context attributes on https://behave.readthedocs.io/en/latest/context_attributes.html#user-attributes
import gmail


def before_all(context):
    args = ['headless', 'window-size=1920,1080'] #if platform != 'darwin' else []
    caps = {
        # -- Chrome Selenoid options
        'browserName': 'chrome',
        'version': '87.0',
        'selenoid:options':
            {
                'enableVNC': True,
                'enableVideo': False
            },
        # -- Chrome browser mobile emulation and headless options
        'goog:chromeOptions': {
            # 'mobileEmulation': {'deviceName': 'iPhone X'},
            # 'window-size': ['1920,1080'],
            'args': args
        }
    }
    '''
        -- Android browser Selenoid options
        "browserName": "android",
        "version": "9.0",
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    
        -- Android native app Selenoid options
        'deviceName': 'android',  # not browserName
        'version': '9.0',
        'app': 'path/to/instagram.apk',
        'appActivity': 'com.instagram.mainactivity.LauncherActivity',
        'appPackage': 'com.instagram.android',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': False
        }
    '''

    # -- Local driver
    context.driver = webdriver.Chrome(desired_capabilities=caps)

    # -- Remote driver
    # context.driver = webdriver.Remote(command_executor='http://67.207.88.128:4444/wd/hub', desired_capabilities=caps)

    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    # read config
    parser = configparser.ConfigParser()
    parser.read('behave.ini')
    context.config = parser
    context.values = {}


def before_feature(context, feature):
    # retry failures
    for scenario in feature.scenarios:
        # if "flaky" in scenario.effective_tags:
        patch_scenario_with_autoretry(scenario, max_attempts=1)


def before_scenario(context, scenario):
    # context.driver.delete_all_cookies()
    print(f'Scenario started: {scenario.name}')
    context.driver.delete_all_cookies()
    gmail.delete_all_emails()


def after_step(context, step) -> None:
    if step.status == 'failed':
        bot = telebot.TeleBot("1461082086:AAGUnZJyEcDwkW1LPHLmezbrXEDzIu6nD8k")
        bot.send_photo(chat_id=-447406725, photo=context.driver.get_screenshot_as_png(),
                       caption=f'{context.scenario.name}:{step.name}\n🐞{step.exception}')
        # bot = telebot.TeleBot("1275523107:AAF_5t_r80J55Pl-JcVeLcVVOsl7kadqAc4")
        # bot.send_photo(chat_id=-407923666, photo=context.driver.get_screenshot_as_png(),
        #                caption=f'{context.scenario.name}:{step.name}\n🐞{step.exception}')


def after_all(context):
    context.driver.quit()
