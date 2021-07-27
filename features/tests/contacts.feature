# Created by Alex Kardash at 24/07/2021
Feature: Проверка формы на странце контактов

  Scenario Outline: контакты emk24
    Given open <url> page
    When open url: "<url>/about/contacts/"
    When enter "test_company_name" in company field
    When enter "test_automation_user_name" in name field
    When enter "+70000000000" in phone field
    When enter "automation.emk@gmail.com" in email field
    When enter "generated_message" in message field
    When click on Send button
    Then text "Ваше сообщение отравлено" is displayed
    Then email with "generated_message" contains "<url>;Организация - test_company_name;[NAME]: test_automation_user_name;[PHONE]: +70000000000;[EMAIL]: automation.emk@gmail.com"

    Examples:
      | url          |
      | emk24.ru     |
      | emk24.by     |
      | emk24.kz     |
      | emk24.com.ua |
