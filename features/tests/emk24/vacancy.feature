# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка вакансии emk24

  Scenario Outline: emk24
    Given open <url> page
    When open url: "<url>/about/vacancies/"
    When click on first vacancy button
    When click on respond vacancy button
    When enter "test_automation_user_name" in name field
    When enter "+70000000000" in phone field
    When enter "automation.emk@gmail.com" in email field
    When enter "generated_message" in message field
    When click on Send button
    Then text "Ваше сообщение отравлено" is displayed
    Then email with "generated_message" contains "<url>;Отклик на вакансию;[NAME]: test_automation;[PHONE]: +70000000000;[EMAIL]: automation.emk@gmail.com"

    Examples:
      | url          |
      | emk24.ru     |
      | emk24.by     |
      | emk24.kz     |
      | emk24.com.ua |
