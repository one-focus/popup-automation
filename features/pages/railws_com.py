from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class RailwsCom(BasePage):
    LINK_ORDER_CALL = By.XPATH, '//button[@data-target="#request_call"]'
    # section order call
    SECTION_ORDER_CALL = By.XPATH, '//div[@id="request_call"]'

    SECTION_TOP_BANNER = By.XPATH, '//section[@class="top_banner"]'
    SECTION_CATALOG = By.XPATH, '//section[@id="catalog"]'
    SECTION_CONTACT = By.XPATH, '//section[@id="kontact"]'

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
        self.on_this_page(self.LINK_ORDER_CALL)
