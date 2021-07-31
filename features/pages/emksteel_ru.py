from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class EmksteelRu(BasePage):
    BUTTON_TOP_REQUEST_CALL = By.XPATH, '(//span[text()="ЗАКАЗАТЬ ЗВОНОК"]/..)[1]'
    BUTTON_BOTTOM_REQUEST_CALL = By.XPATH, '(//span[text()="ЗАКАЗАТЬ ЗВОНОК"]/..)[2]'
    BUTTON_REQUEST_CALL_BACK = By.XPATH, '//span[text()="Заказать обратный звонок"]/..'

    SECTION_1 = By.XPATH, '//h3[text()="Предварительный расчет стоимости"]/../..'
    BUTTON_MORE_INFO = By.XPATH, '//span[text()="УЗНАТЬ ПОДРОБНОСТИ"]/..'
    BUTTON_SEND_EMAIL = By.XPATH, '//span[text()="ОТПРАВИТЬ ПИСЬМО"]/..'
    # section order call
    SECTION_REQUEST_CALL = By.XPATH, '(//h4[text()=" Заказать обратный звонок"]/..)[1]'

    SECTION_CATALOG = By.XPATH, '//section[@id="catalog"]'
    SECTION_PRODUCT = By.XPATH, '//section[@id="prod"]'

    # quiz
    BUTTON_PRICE_CALCULATION = By.XPATH, '//section[@class="section hide-for-small"]//span[text()="РАСЧЕТ СТОИМОСТИ"]/..'
    BUTTON_START = By.XPATH, '//button[contains(text(),"Начать")]'
    BUTTON_NEXT = By.XPATH, '//span[contains(text(),"Далее")]/..'

    BUTTON_BLACK = By.XPATH, '//div[contains(text(),"Черный ")]'
    CHECKBOX_YES = By.XPATH, '//input[@value="Да"]/..'

    INPUT_FILE = By.XPATH, '//label[@class="upload control"]//input[@type="file"]'

    FIELD_NAME_QUIZ = By.XPATH, '//input[@id="name"]'
    FIELD_EMAIL_QUIZ = By.XPATH, '//input[@id="email"]'
    FIELD_PHONE_QUIZ = By.XPATH, '//input[@id="VuePhoneNumberInput_phone_number"]'
    DROPDOWN_COUNTRY = By.XPATH, '//input[@id="VuePhoneNumberInput_country_selector"]'
    COUNTRY_RUSSIA = By.XPATH, '//div[contains(text(),"Russia (Россия)")]/..'
    BUTTON_SEND_QUIZ = By.XPATH, '//span[text()="Отправить"]/..'
    # modal dialog section
    SECTION_SEND_REQUEST = By.XPATH, '//div[@id="send_request"]'
    FIELD_NAME = By.XPATH, '//*[@name="your-name"]'
    FIELD_PHONE = By.XPATH, '//*[contains(@name,"mask-")]'
    FIELD_COMPANY_NAME = By.XPATH, '//*[@name="your-company"]'
    FIELD_EMAIL = By.XPATH, '//*[@name="your-email"]'
    FIELD_MESSAGE = By.XPATH, '//*[@name="your-message"]'

    BUTTON_SEND = By.XPATH, '//input[@type="submit"]'
    BUTTON_SEND_REQUEST = By.XPATH, '//button[@data-target="#send_request"]'

    def _verify_page(self):
        self.on_this_page(self.BUTTON_REQUEST_CALL_BACK)
