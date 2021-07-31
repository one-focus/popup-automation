from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class A1ValvesCom(BasePage):
    BUTTON_ORDER_CALL = By.XPATH, '//button[@data-target="#request_call"]'
    # section order call
    SECTION_TOP_MENU = By.XPATH, '//div[@id="up_top"]'
    SECTION_REQUEST_CALL = By.XPATH, '//div[@id="request_call"]'

    SECTION_CATALOG = By.XPATH, '//section[@id="catalog"]'
    SECTION_PRODUCT = By.XPATH, '//section[@id="prod"]'

    # modal dialog section
    SECTION_SEND_REQUEST = By.XPATH, '//div[@id="send_request"]'
    FIELD_NAME = By.XPATH, '//*[@name="name"]'
    FIELD_PHONE = By.XPATH, '//*[@name="phone"]'
    FIELD_COMPANY_NAME = By.XPATH, '//*[@name="company"]'
    FIELD_EMAIL = By.XPATH, '//*[@name="email"]'
    FIELD_MESSAGE = By.XPATH, '//*[@name="comment"]'

    BUTTON_SEND = By.XPATH, '//button[@type="submit"]'
    BUTTON_SEND_REQUEST = By.XPATH, '//button[@data-target="#send_request"]'


    def _verify_page(self):
        self.on_this_page(self.BUTTON_ORDER_CALL)
