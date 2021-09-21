# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка сайта a1-valves.com

  Scenario Outline: a1-valves.com заказать звонок
    Given open a1-valves.com page
    When click on order call button in "<section>"
    When enter "generated_test_automation_email_call_a1" in name field in "request call section"
    When enter "+70000000000" in phone field in "request call section"
    When click on send button in "request call section"
    Then email with "generated_test_automation_email_call_a1" contains "Телефон : +70000000000" in 900 sec

    Examples:
      | section          |
      | top menu section |
      | catalog section  |

  Scenario Outline: a1-valves.com оставить заявку
    Given open a1-valves.com page
    When wait 2 sec
    When click on send request button in "<section>"
    When enter "generated_test_automation_email_a1" in name field in "send request section"
    When enter "+70000000000" in phone field in "send request section"
    When enter "test_automation_company_name" in company name field in "send request section"
    When enter "test_automation_comment" in message field in "send request section"
    When enter "automation.emk@gmail.com" in email field in "send request section"
    When click on send button in "send request section"
    Then email with "generated_test_automation_email_a1" contains "Email : automation.emk@gmail.com;Телефон : +70000000000;Комментарий : test_automation_commen" in 900 sec

    Examples:
      | section         |
      | catalog section |
      | product section |
