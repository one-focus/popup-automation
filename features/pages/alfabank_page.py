from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AlfaBank(BasePage):

    @property
    def _elements_map(self):
        return {
            'iframe': (By.TAG_NAME, 'iframe'),

            # 'cardnumber div': (By.XPATH, '//div[@class="card__number"]/span'),
            'cardnumber field': (By.ID, 'ccnumber'),
            'expired field': (By.ID, 'expired'),
            'expired error': (By.XPATH, '//span[@data-langlbl="err_expiry"]'),
            'cardholder field': (By.ID, 'iTEXT'),
            'cvc field': (By.ID, 'iCVC'),
            'pay button': (By.ID, 'buttonPayment'),

            '3d secure page': (By.XPATH, '//img[@class="bankLogoImageClass"]'),
            'repeat button': (By.XPATH, '//*[@id="statusContainer"]//button[1]'),
            'cancel button': (By.XPATH, '//*[@id="statusContainer"]//button[2]'),
        }

    def _verify_page(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.on_this_page('cardnumber field')
