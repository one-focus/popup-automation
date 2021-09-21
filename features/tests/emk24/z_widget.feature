# Created by Alex Kardash at 24/07/2021
Feature: Проверка zwidget emk24

  Scenario: emk24
    Given open emk24.ru page
    When click on open z widget button
    When wait 2 sec
    When enter "70000000000" in z widget phone field
    When click on wait for call button
    When click on terms checkbox
    Then text "Спасибо за заявку!" is displayed
    Then email with "Widget: Обратный звонок" contains "Номер: 70000000000" in 900 sec
