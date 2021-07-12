import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CloudPayments(BasePage):

    @property
    def _elements_map(self):
        return {
            'iframe': (By.XPATH, '//iframe[contains(@class,"with-appled")]'),

            'cardnumber field': (By.ID, 'cardNumber'),
            'cardnumber label': (By.XPATH, '//label[@for="cardNumber"]'),
            'month field': (By.ID, 'inputMonth'),
            'year field': (By.ID, 'inputYear'),
            'cardholder field': (By.ID, 'cardHolder'),
            'cvc field': (By.ID, 'cardCvv'),
            'pay button': (By.XPATH, '//*[@id="sizingContainer"]//button'),
            'continue button': (By.XPATH, '//div[@id="statusContainer"]//button'),

            '3d secure widget': (By.ID, 'pwdInputVisible'),
            'repeat button': (By.XPATH, '//*[@id="statusContainer"]//button[1]'),
            'cancel button': (By.XPATH, '//*[@id="statusContainer"]//button[2]'),
        }

    def _verify_page(self):
        element = self.get_element('iframe', timeout=20)
        self.driver.switch_to.frame(element)
