# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка сайта forging.emk24.su

  Scenario Outline: forging.emk24.su секция 1 и 2
    Given open forging.emk24.su page
    When click on <button> in "<section>"
    When enter "generated_test_automation_email" in name field in "modal section"
    When enter "+70000000000" in phone field in "modal section"
    When enter "test_automation_company_name" in company name field in "modal section"
    When enter "automation.emk@gmail.com" in email field in "modal section"
    When enter "test_automation_comment" in message field in "modal section"
    When click on leave order button in "modal section"
    Then text "СПАСИБО ЗА ЗАЯВКУ!" is displayed
    Then email with "generated_test_automation_email" contains "[FORM]: Оставить заявку.;[PHONE]: +70000000000;[EMAIL]: automation.emk@gmail.com;[BODY]: Компания: test_automation_company" in 240 sec
    Examples:
      | button             | section   |
      | leave order button | 1 section |
      | basket button      | 2 section |

  Scenario: forging.emk24.su секция 3
    Given open forging.emk24.su page
    When enter "generated_test_automation_email" in name field in "3 section"
    When enter "+70000000000" in phone field in "3 section"
    When enter "test_automation_company_name" in company name field in "3 section"
    When enter "automation.emk@gmail.com" in email field in "3 section"
    When enter "test_automation_comment" in message field in "3 section"
    When click on send button in "3 section"
    Then text "СПАСИБО ЗА ЗАЯВКУ!" is displayed
    Then email with "generated_test_automation_email" contains "[FORM]: Форма заказа внизу;[PHONE]: +70000000000;[EMAIL]: automation.emk@gmail.com;[BODY]: Компания: test_automation_company" in 240 sec

  Scenario: forging.emk24.su заказать звонок
    Given open forging.emk24.su page
    When click on order call link
    When enter "generated_test_automation_email_call_ord" in name field in "order call section"
    When enter "+70000000000" in phone field in "order call section"
    When click on send button in "order call section"
    Then text "СПАСИБО ЗА ЗАЯВКУ!" is displayed
    Then email with "generated_test_automation_email_call_ord" contains "[FORM]: Заказать обратный звонок;[PHONE]: +70000000000" in 240 sec