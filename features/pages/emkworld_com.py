from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class EmkworldCom(BasePage):
    BUTTON_TOP_REQUEST_A_CALLBACK = By.XPATH, '(//span[text()="REQUEST A CALLBACK"]/..)[1]'
    SECTION_CALLBACK_DIALOG = By.XPATH, '//h4[text()=" Request a callback "]/..'
    SECTION_REQUEST_DIALOG = By.XPATH, '//h4[text()=" Leave a request to receive a quote "]/..'
    SECTION_REQUEST_PRICE_DIALOG = By.XPATH, '//h4[text()=" Request a price list "]/..'
    SECTION_CONTACT = By.XPATH, '//h2[@id="contacts"]/ancestor::section'

    FIELD_NAME = By.XPATH, '//*[@name="your-name"]'
    FIELD_PHONE = By.XPATH, '//*[@name="your-telephone"]'
    FIELD_COMPANY_NAME = By.XPATH, '//*[@name="your-company"]'
    FIELD_EMAIL = By.XPATH, '//*[@name="your-email"]'
    FIELD_MESSAGE = By.XPATH, '//*[@name="your-message"]'

    BUTTON_LEAVE_REQUEST = By.XPATH, '//span[text()="LEAVE REQUEST"]/..'
    BUTTON_PRICE = By.XPATH, '//span[text()="PRICE"]/..'
    BUTTON_ORDER_CALCULATION = By.XPATH, '//span[text()="ORDER CALCULATION"]/..'
    BUTTON_MIDDLE_REQUEST_A_CALLBACK = By.XPATH, '(//span[text()="REQUEST A CALLBACK"]/..)[2]'
    BUTTON_CALL_ME = BUTTON_SEND = By.XPATH, '//input[@type="submit"]'
    BUTTON_SEND_A_MESSAGE = By.XPATH, '//span[text()="SEND A MESSAGE"]/..'
    BUTTON_BOTTOM_REQUEST_A_CALLBACK = By.XPATH, '(//span[text()="REQUEST A CALLBACK"]/..)[3]'

    def _verify_page(self):
        self.on_this_page(self.BUTTON_TOP_REQUEST_A_CALLBACK)
