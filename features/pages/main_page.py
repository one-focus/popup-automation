from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def _elements_map(self):
        return {
            "activate button": (By.XPATH,
                                '(//*[@data-id="email"]|//section[@id="prise_1"]//div[@class="prise_one silver"]//a|(//div[@class="pris_one silver"]//a)[1])'),
            "email field": (By.NAME, 'email'),
            "next button": (By.XPATH, '(//button[contains(@type,"submit")]|//button[@class="bubbly-button pink_but pulse"])'),

            "policy link": (By.XPATH, '//a[@href="https://zhiry-net.ru/about/privacy/"]'),
            "oferta link": (By.XPATH, '//a[@href="https://zhiry-net.ru/about/oferta/"]'),
            "quiz button": (By.XPATH, '(//a[@data-action="link"])[1]')
        }

    def _verify_page(self):
        pass
        # self.on_this_page('oferta link', "policy link")
