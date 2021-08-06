# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка кнопки Купить в 1 клик

  @test
  Scenario Outline: Купить в 1 клик emk24
    Given open <url> page
    When click on first left menuitem
    When enter "1" in first count field
    When click on first buy in one click button
    When wait 1 sec
    When enter "test_automation_contact_name" in name field
    When enter "+70000000000" in phone field
    When enter "automation.emk@gmail.com" in email field
    When enter "generated_comment_1_click" in comment field
    When click on Send button

    Then text "Спасибо, ваш заказ принят" is displayed

    Then email with "generated_comment_1_click" contains "Заказ в 1 клик!;[NAME]: test_automation_contact_name;[PHONE]: +70000000000;[EMAIL]: automation.emk@gmail.com" in 600 sec

    Examples:
      | url          |
      | emk24.ru     |
      | emk24.by     |
      | emk24.kz     |
      | emk24.com.ua |
