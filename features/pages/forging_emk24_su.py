from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class ForgingEmk24Su(BasePage):

    BUTTON_LEAVE_ORDER = By.XPATH, '//div[@class="right-image"]//button[text()="Оставить заявку"]'
    FIELD_NAME = '//form[contains(@class,"form3")]//input[@name="name"]'
    FIELD_PHONE = '//form[contains(@class,"form3")]//input[@name="phone"]'
    FIELD_COMPANY = '//form[contains(@class,"form3")]//input[@name="company"]'
    FIELD_MESSAGE = '//form[contains(@class,"form3")]//input[@name="msg"]'

    BUTTON_SEND = By.XPATH, '//form[contains(@class,"form3")]//button[@type="submit"]'

    def _verify_page(self):
        self.on_this_page(self.BUTTON_LEAVE_ORDER)
