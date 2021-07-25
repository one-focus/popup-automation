from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class EmkMetRuPage(BasePage):
    # first form
    SECTION_1 = By.XPATH, '//form[@name="fast"]'
    SECTION_2 = By.XPATH, '//form[@name="calc"]'
    SECTION_3 = By.XPATH, '//form[@name="services"]'
    SECTION_4 = By.XPATH, '//form[@name="multi_var"]'

    # order item page
    FIELD_COMPANY = By.XPATH, '//input[@name="company"]'
    FIELD_PRODUCT = By.XPATH, '//input[@name="products"]'
    FIELD_EMAIL = By.XPATH, '//input[@name="email"]'
    FIELD_PHONE = By.XPATH, '//input[@name="phone"]'
    BUTTON_GET_PRICE = By.XPATH, '//button[@type="submit"]'

    # section 2 calc
    BUTTON_FIRST_METAL = By.XPATH, '//a[@aria-controls="multiCollapseExample1" and @aria-expanded="false"]'
    BUTTON_SECOND_METAL = By.XPATH, '//a[@aria-controls="multiCollapseExample2" and @aria-expanded="false"]'
    BUTTON_THIRD_METAL = By.XPATH, '//a[@aria-controls="multiCollapseExample3" and @aria-expanded="false"]'
    BUTTON_FOURTH_METAL = By.XPATH, '//a[@aria-controls="multiCollapseExample4" and @aria-expanded="false"]'
    BUTTON_FIFTHS_METAL = By.XPATH, '//a[@aria-controls="multiCollapseExample5" and @aria-expanded="false"]'
    BUTTON_FIRST_PRODUCT = By.XPATH, '//input[@id="prod1"]'
    BUTTON_SECOND_PRODUCT = By.XPATH, '//input[@id="prod12"]'
    BUTTON_THIRD_PRODUCT = By.XPATH, '//input[@id="prod24"]'
    BUTTON_FOURTH_PRODUCT = By.XPATH, '//input[@id="prod31"]'
    BUTTON_FIFTHS_PRODUCT = By.XPATH, '//input[@id="prod39"]'
    FIELD_COMMENT = By.XPATH, '//textarea[@name="comment"]'

    def _verify_page(self):
        self.on_this_page(self.SECTION_1, self.SECTION_2, self.SECTION_3, self.SECTION_4)
