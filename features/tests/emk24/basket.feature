# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка корзины emk24

  Scenario Outline: корзина emk24
    Given open <url> page
    When click on first left menuitem
    When enter "1" in first count field
    When click on first basket button
    When wait 5 sec
    Given open url: "<url>/order/"
    When enter "test_automation_comment" in comment field
    When click on checkout button

    When enter "123456789" in INN field
    When enter "test_automation_company_name" in company field
    When enter "test_automation_contact_name" in contact name field
    When enter "+70000000000" in phone field
    When enter "automation.emk@gmail.com" in email field
    When click on checkout button
    Then text "Спасибо за заказ!" is displayed
    When remember order number label as "order_number"

    Then email with "order_number" contains "Ваша заявка номер order_number" in 900 sec

    Examples:
      | url          |
      | emk24.ru     |
      | emk24.by     |
      | emk24.kz     |
      | emk24.com.ua |
