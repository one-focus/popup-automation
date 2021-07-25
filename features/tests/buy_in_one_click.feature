# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка кнопки Купить в 1 клик

  Scenario Outline: Купить в 1 клик emk24
    Given open <url> page
    When click on first left menuitem
    When enter "1" in first count field
    When click on first buy in one click button

    When enter "test_automation_contact_name" in contact name field
    When enter "+70000000000" in phone field
    When enter "automation.emk@gmail.com" in email field
    When enter "generated_comment" in comment field
    When click on Send button

    Then text "Спасибо, ваш заказ принят" is displayed

    Then email with "order_number" contains "Ваша заявка номер order_number"

    Examples:
      | url          |
      | emk24.ru     |
      | emk24.by     |
      | emk24.kz     |
      | emk24.com.ua |
