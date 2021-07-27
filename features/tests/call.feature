# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка кнопки заказать звонок

  Scenario Outline: Заказать звонок emk24
    Given open <url> page
    When click on call request button
    When enter "+70000000000" in phone field
    When wait 1 sec
    When click on Send button
    Then text "Ваше сообщение отравлено" is displayed
    Then email with "[BODY]: Обратный звонок (заявка) <url>" contains "[PHONE]: +70000000000"

    Examples:
      | url          |
      | emk24.ru     |
      | emk24.by     |
      | emk24.kz     |
      | emk24.com.ua |
