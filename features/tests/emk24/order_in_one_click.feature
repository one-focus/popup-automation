# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка кнопки Заказать в 1 клик emk24

  Scenario Outline: emk24
    Given open <url> page
    When click on order in 1 click button
    When enter "generated_test_automation_email_order_1_click" in message field
    When click on Continue button
    When enter "test_automation_user_name" in name field
    When enter "test_company_name" in company field
    When enter "+70000000000" in phone field
    When enter "automation.emk@gmail.com" in email field
    When click on Send button
    Then text "Спасибо за заявку!" is displayed

    Then email with "generated_test_automation_email_order_1_click" contains "<url>;Заказ в 1 клик!;test_automation_user_name;test_company_name;+70000000000;automation.emk@gmail.com" in 240 sec

    Examples:
      | url          |
      | emk24.ru     |
      | emk24.by     |
      | emk24.kz     |
      | emk24.com.ua |
