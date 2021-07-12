import abc

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        pass

    def on_this_page(self, *args):
        for element_name in args:
            self.get_element(element_name)

    def scroll_to(self, element_name):
        action = ActionChains(self.driver)
        element = self.get_element(element_name)
        action.move_to_element(element).perform()

    def click_on(self, element_name, timeout=10):
        element = self.get_clickable_element(element_name, timeout)
        # from selenium.webdriver import ActionChains
        # hover = ActionChains(self.driver).move_to_element(element)
        # hover.perform()
        element.click()

    def type_in(self, element_name, text):
        element = self.get_clickable_element(element_name)
        # from selenium.webdriver import ActionChains
        # hover = ActionChains(self.driver).move_to_element(element)
        # hover.perform()
        element.clear()
        element.send_keys(text)

    def get_text(self, element_name):
        return self.get_element(element_name).text

    @property
    @abc.abstractmethod
    def _elements_map(self) -> dict:
        return {}

    def get_element(self, element_name, timeout=5):
        locator = self._elements_map.get(element_name)
        if locator is None:
            raise RuntimeError(f'Элемент "{element_name}" не описан в списке "elements_map" на экране')
        expected_condition = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(
            expected_condition, message=f'Не могу найти элемент: "{element_name}"  за {timeout} сек')

    def get_clickable_element(self, element_name, timeout=10):
        locator = self._elements_map.get(element_name)
        if locator is None:
            locator = (By.XPATH, f'//*[text() = "{element_name}"]')
        expected_condition = ec.element_to_be_clickable(locator)
        return WebDriverWait(self.driver, timeout).until(
            expected_condition, message=f'Не могу найти элемент: {element_name} за {timeout} сек')
