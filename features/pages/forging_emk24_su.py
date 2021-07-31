from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class ForgingEmk24Su(BasePage):
    LINK_ORDER_CALL = By.XPATH, '//a[text()="Заказать звонок"]'
    # section order call
    SECTION_ORDER_CALL = By.XPATH, '//div[@id="order-call"]'

    # section 1
    SECTION_1 = By.XPATH, '//div[@class="right-image"]'
    BUTTON_LEAVE_ORDER = By.XPATH, '//button[text()="Оставить заявку"]'
    FIELD_NAME = By.XPATH, '//*[@name="name"]'
    FIELD_PHONE = By.XPATH, '//*[@name="phone"]'
    FIELD_COMPANY_NAME = By.XPATH, '//*[@name="company"]'
    FIELD_EMAIL = By.XPATH, '//*[@name="email"]'
    FIELD_MESSAGE = By.XPATH, '//*[@name="msg"]'

    BUTTON_SEND = By.XPATH, '//button[@type="submit"]'

    # section 2
    SECTION_2 = By.XPATH, '//div[@class="block5 table1"]'
    BUTTON_BASKET = By.XPATH, '//img[@src="img/cart.png"]'

    # section contacts
    SECTION_3 = By.XPATH, '//div[@id="contacts"]'
    SECTION_MODAL = By.XPATH, '//div[@id="order"]'

    def _verify_page(self):
        self.on_this_page(self.BUTTON_LEAVE_ORDER)
