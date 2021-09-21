# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка кнопки скачать снандарт emk24

  Scenario Outline: Скачать стандарт emk24
    Given open <url> page
    When open url: "<url>/wiki/ansi_standarty/"
    When click on first standard button
    When click on download pdf button
    When enter "<inn>" in inn field
    When enter "+70000000000" in phone field
    When enter "automation.emk@gmail.com" in email field
    When click on Send button
    Then text "Проверьте, пожалуйста" is displayed
    Then email with "<inn>" contains "<url>;Запрос на скачивание стандарта;[PHONE]: +70000000000;[EMAIL]: automation.emk@gmail.com" in 900 sec

    Examples:
      | url          | inn       |
      | emk24.ru     | 013456789 |
      | emk24.by     | 023456789 |
      | emk24.kz     | 033456789 |
      | emk24.com.ua | 043456789 |
