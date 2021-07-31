from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class Emk24Page(BasePage):
    BUTTON_CALL_REQUEST = By.XPATH, '//div[@class="phone-block-links"]/a[contains(@href,"callme.php")]'

    MENUITEM_FIRST_LEFT = By.XPATH, '//div[contains(@class,"header-submenu main-page-menu")]//ul[@class="submenu-list menu-tab js-menu__tab open"]//a[@class="submenu-title__link"]'
    BUTTON_ORDER_IN_1_CLICK = By.XPATH, '//ul[@class="nav nav-tabs"]//a[@href="/order-in-1-click/"]'
    FIELD_MESSAGE = By.XPATH, '//*[@name="comment"]|//textarea[@name="FIELD[PREVIEW_TEXT]"]'
    FIELD_NAME = By.XPATH, '//input[@name="fio"]|//input[@name="PROPERTY_VALUES[UNAME]"]|//input[@placeholder="Имя"]'
    FIELD_COMPANY = By.XPATH, '//*[@name="company"]|//*[@name="FIELDS[WORK_COMPANY]"]|//input[@name="PROPERTY_VALUES[COMPANY]"]'
    FIELD_PHONE = By.XPATH, '//*[@name="phone"]|//*[@name="FIELDS[WORK_PHONE]"]|//input[@name="PROPERTY_VALUES[PHONE]"]|//input[@placeholder="Телефон"]'
    FIELD_EMAIL = By.XPATH, '//input[@name="email"]|//*[@name="mail"]|//input[@name="FIELDS[EMAIL]"]|//input[@name="PROPERTY_VALUES[EMAIL]"]|//input[@placeholder="Email"]'
    BUTTON_UPLOAD_FILE = By.ID, 'file_input_mfifiles_send'
    BUTTON_CONTINUE = By.XPATH, '//div[@class="step1"]//span[@class="but_big_card js-continue"]'
    BUTTON_SEND = By.XPATH, '//div[@class="step2"]//span[@class="but_big_card js-continue"]|//button[contains(@data-event,"USER_SEND_FORM_")]|//input[@type="submit"]'
    FORM_MODAL = By.XPATH, '//div[@role="dialog" and contains(@style,"display: block;")]'
    # order item page
    FIELD_FIRST_COUNT = By.NAME, 'count1'
    BUTTON_FIRST_BASKET = By.CLASS_NAME, 'add-to-basket'
    BUTTON_FIRST_BUY_IN_ONE_CLICK = By.XPATH, '//span[contains(@class,"buy_one_click_btn")]'
    BUTTON_FIRST_SPLAV = BUTTON_FIRST_STANDARD = By.XPATH, '//a[@class="wiki-title nlink"]'
    BUTTON_DOWNLOAD_PDF = By.XPATH, '//ul[@class="download-nav"]//a'
    BUTTON_CHECKOUT = By.XPATH, '//span[@class="make-purchase"]/../..|//div[@class="form-group form-group-action"]//button'

    # checkout page
    FIELD_COMMENT = By.XPATH, '//*[@name="COMMENT"]|//textarea[@name="comment"]'
    FIELD_INN = By.XPATH, '//*[contains(@name,"S[INN]")]'
    FIELD_CONTACT_NAME = By.NAME, 'FIELDS[NAME]'
    LABEL_ORDER_NUMBER = By.XPATH, '//div[text()="Номер вашего заказа"]/../div[@class="basket-success-params-val"]'

    # right sidebar
    BUTTON_CLOSE_RIGHT_SIDEBAR = By.XPATH, '//div[contains(@class,"z-widget-sidebar-close")]'

    # Jivo dialog
    WIDGET_JIVO = By.XPATH, '//jdiv[contains(@style,"Label_OPEN_WIDGET")]'
    BUTTON_CLOSE_JIVO_CHAT = By.ID, 'jivo_close_button'

    # Vacancy
    BUTTON_FIRST_VACANCY = By.XPATH, '//div[@class="slide-box js-accordion"]//span[@class="dotted-link"]'
    BUTTON_RESPOND_VACANCY = By.XPATH, '//div[@class="slide-contnt js-accordion__body" and @style="display: block;"]//a[contains(text(),"Откликнуться на вакансию")]'

    BUTTON_AGREE_COOKIES = By.CLASS_NAME, 'agree_cookie'

    # zwidget
    BUTTON_OPEN_Z_WIDGET = By.XPATH, '//div[@id="zcwMiniButton"]'
    FIELD_Z_WIDGET_PHONE = By.XPATH, '//*[@name="n"]'
    CHECKBOX_TERMS = By.XPATH, '//input[@id="terms1"]'
    BUTTON_WAIT_FOR_CALL = By.XPATH, '//button[text()="Жду звонка!"]'
    def _verify_page(self):
        self.on_this_page(self.BUTTON_ORDER_IN_1_CLICK)

    def click_on(self, element_name, section=None):
        try:
            super(Emk24Page, self).click_on(element_name)
        except ElementClickInterceptedException:
            try:
                super(Emk24Page, self).click_on(self.BUTTON_AGREE_COOKIES)
                super(Emk24Page, self).click_on(element_name)
            except ElementClickInterceptedException:
                if self.is_element_displayed(self.BUTTON_CLOSE_RIGHT_SIDEBAR, 0):
                    self.click_on(self.BUTTON_CLOSE_RIGHT_SIDEBAR)
                    super(Emk24Page, self).click_on(element_name)
                if self.is_element_displayed(self.WIDGET_JIVO, 0):
                    self.click_on(self.BUTTON_CLOSE_JIVO_CHAT)
                    super(Emk24Page, self).click_on(element_name)
                    sleep(0.2)
        locator = self.get_element_by_name(element_name)
        if locator == self.BUTTON_FIRST_BUY_IN_ONE_CLICK:
            for i in range(10):
                if self.is_element_displayed(self.FORM_MODAL):
                    break
                else:
                    self.driver.refresh()
                    super(Emk24Page, self).click_on(element_name)
            else:
                raise RuntimeError(
                    "Форма заказа не отображается на странице после 10 нажатий на кнопку Купить в 1 клик")
