import datetime

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    @property
    def _elements_map(self):
        return {
            'confirm checkbox': (By.ID, 'usl'),
            'continue button': (By.XPATH, '(//*[@id="payButton"]|//a[@class="rbs__payment-link ok"])'),

            'policy link': (By.XPATH, '//a[@href="/about/oferta/"]'),
            'oferta link': (By.XPATH, '//a[@href="/about/oferta/"]')
        }

    def _verify_page(self):
        self.on_this_page('confirm checkbox')
