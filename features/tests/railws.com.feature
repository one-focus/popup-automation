# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка сайта railws.com

  Scenario: railws.com заказать звонок
    Given open railws.com page
    When click on order call link
    When enter "generated_test_automation_email_order_railws" in name field in "order call section"
    When enter "+9000000000" in phone field in "order call section"
    When click on send button in "order call section"
    Then email with "generated_test_automation_email_order_railws" contains "Телефон : +7 900 000 00 00" in 900 sec

  Scenario Outline: railws.com оставить заявку
    Given open railws.com page
    When click on send request button in "<section>"
    When enter "generated_test_automation_email_leave_call" in name field in "send request section"
    When enter "automation.emk@gmail.com" in email field in "send request section"
    When enter "+9000000000" in phone field in "send request section"
    When enter "test_automation_company_name" in company name field in "send request section"
    When enter "test_automation_comment" in message field in "send request section"
    When click on send button in "send request section"
    Then email with "generated_test_automation_email_leave_call" contains "Email : automation.emk@gmail.com;Телефон : +7 900 000 00 00;Комментарий : test_automation_comment" in 900 sec

    Examples:
      | section            |
      | top banner section |
      | catalog section    |
      | contact section    |
