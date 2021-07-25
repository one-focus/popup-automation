import configparser

import allure
from selenium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

# TODO check all context attributes on https://behave.readthedocs.io/en/latest/context_attributes.html#user-attributes
import gmail


def before_all(context):
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
        # 'goog:chromeOptions': {
        #     # 'mobileEmulation': {'deviceName': 'iPhone X'},
        #     'args': ['headless']
        # }
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

    context.driver.implicitly_wait(5)
    context.driver.maximize_window()
    # read config
    parser = configparser.ConfigParser()
    parser.read('behave.ini')
    context.config = parser
    context.values = {}
    gmail.delete_all_emails()

def before_feature(context, feature):
    # retry failures
    for scenario in feature.scenarios:
        # if "flaky" in scenario.effective_tags:
        patch_scenario_with_autoretry(scenario, max_attempts=1)


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_step(context, step) -> None:
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name='bug.png',
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    context.driver.quit()
