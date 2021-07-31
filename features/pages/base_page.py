import abc
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, \
    ElementClickInterceptedException, NoSuchElementException
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

    def hover_element(self, locator):
        element = self.get_clickable_element(locator)
        Hover = ActionChains(self.driver).move_to_element(element)
        Hover.perform()

    def click_on(self, element_name, section=None):
        try:
            self.hover_element(element_name)
            self.get_clickable_element(element_name).click()
        except StaleElementReferenceException:
            sleep(1)
            self.get_clickable_element(element_name).click()

    def type_in(self, element_name, text):
        self.get_element(element_name).clear()
        self.get_element(element_name).send_keys(text)

    def get_text(self, element_name):
        return self.get_element(element_name).text

    def get_element_by_name(self, element):
        if type(element) is str:
            name_array = element.split()
            name_array.insert(0, name_array.pop())
            try:
                return getattr(self, '_'.join(name_array).upper())
            except Exception:
                return (By.XPATH, f'//*[text()="{element}"]|//*[@value="{element}"]')
        return element

    def get_element(self, element_name, timeout=5):
        locator = self.get_element_by_name(element_name)
        expected_condition = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(
            expected_condition,
            message=f'Не могу найти {element_name} в течение {timeout} сек')

    def get_clickable_element(self, element_name, timeout=5):
        locator = self.get_element_by_name(element_name)
        expected_condition = ec.element_to_be_clickable(locator)
        return WebDriverWait(self.driver, timeout).until(
            expected_condition,
            message=f'Не могу найти {element_name} в течение {timeout} сек')

    def get_element_in_section(self, locator_name, section_name):
        section_name = section_name if section_name.endswith('section') else f'{section_name} section'
        section_element = self.get_element(section_name)
        if self.get_element_by_name(locator_name)[0] == 'xpath':
            try:
                return section_element.find_element_by_xpath(
                    f'.{self.get_element_by_name(locator_name)[1]}')
            except NoSuchElementException:
                raise RuntimeError(f'Unable to locate {locator_name} in {section_name}')
        else:
            raise RuntimeError('Use XPATH locator only for section element')

    def is_element_displayed(self, element_name, timeout=5):
        locator = self.get_element_by_name(element_name)
        try:
            self.get_element(locator, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def is_element_invisible(self, element_name, timeout=5):
        locator = self.get_element_by_name(element_name)
        try:
            expected_condition = ec.invisibility_of_element_located(locator)
            WebDriverWait(self.driver, timeout).until(
                expected_condition,
                message=f'Элемент {element_name} отображается в течение {timeout} сек"')
            return True
        except TimeoutException:
            return False
