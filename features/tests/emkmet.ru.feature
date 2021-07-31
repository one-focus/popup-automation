# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка сайта emkmet.ru

  Scenario Outline: emkmet_ru секция 1 и 4
    Given open emkmet.ru page
    When enter "generated_company_name" in company field in "<section>"
    When enter "test_automation_product" in product field in "<section>"
    When enter "automation.emk@gmail.com" in email field in "<section>"
    When enter "70000000000" in phone field in "<section>"
    When click on get price button in "<section>"
    Then text "СПАСИБО ЗА ЗАЯВКУ!" is displayed

    Then email with "generated_company_name" contains "Компания : generated_company_name;Продукты : test_automation_product;Email : automation.emk@gmail.com;Телефон : +7000000000"" in 240 sec

    Examples:
      | section   |
      | 1 section |
      | 4 section |


  Scenario: emkmet_ru секция 2
    Given open emkmet.ru page
    When click on first metal button in "2 section"
    When click on third metal button in "2 section"
    When click on fourth metal button in "2 section"
    When click on fifths metal button in "2 section"
    When click on Черный: Балка двутавровая in "2 section"
    When click on Нержавейка: Балка двутавровая in "2 section"
    When click on Пищевая нержавейка: Фланцы пищевые in "2 section"
    When click on Никель: Фитинги in "2 section"
    When click on Алюминий: Рифленые листы in "2 section"

    When enter "generated_comment" in comment field in "2 section"
    When enter "automation.emk@gmail.com" in email field in "2 section"
    When enter "70000000000" in phone field in "2 section"
    When click on get price button in "2 section"
    Then text "СПАСИБО ЗА ЗАЯВКУ!" is displayed

    Then email with "generated_comment" contains "Email : automation.emk@gmail.com;Телефон : +7000000000;Черный: Балка двутавровая;Нержавейка: Балка двутавровая;Пищевая нержавейка: Фланцы пищевые;Никель: Фитинги;Алюминий: Рифленые листы"" in 240 sec

  Scenario: emkmet_ru секция 3
    Given open emkmet.ru page
    When click on Услуги по металлообработке in "3 section"
    When click on Услуги по испытанию продукции in "3 section"
    When click on Услуги испытания продукции in "3 section"
    When enter "automation.emk@gmail.com" in email field in "3 section"
    When enter "70000000000" in phone field in "3 section"
    When enter "generated" in email field in "2 section"
    When click on get price button in "3 section"

    Then email with "generated" contains "Email : automation.emk@gmail.com;Телефон : +7000000000;Услуги по металлообработке;Услуги по испытанию продукции;Услуги испытания продукции"" in 240 sec

