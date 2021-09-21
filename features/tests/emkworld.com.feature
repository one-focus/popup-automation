# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка сайта emkworld.com

  Scenario Outline: emkworld.com заказать звонок
    Given open emkworld.com page
    When click on <button>
    When wait 2 sec
    When enter "generated_test_automation_email_call_order" in name field in "callback dialog section"
    When enter "test_automation_company_name" in company name field in "callback dialog section"
    When enter "+70000000000" in phone field in "callback dialog section"
    When click on call me button in "callback dialog section"
#    Then text "Thank you for your message" is displayed
    Then email with "generated_test_automation_email_call_order" contains "+70000000000;Тема: Request from test_automation_company_name;Please, call me back +70000000000" in 900 sec

    Examples:
      | button                           |
      | top request a callback button    |
      | bottom request a callback button |

  Scenario Outline: emkworld.com оставить заявку
    Given open emkworld.com page
    When click on <button>
    When wait 2 sec
    When enter "generated_test_automation_email_leave_order_emk" in name field in "<section>"
    When enter "test_automation_company_name" in company name field in "<section>"
    When enter "automation.emk@gmail.com" in email field in "<section>"
    When enter "+70000000000" in phone field in "<section>"
    When enter "test_autoamtion_message" in message field in "<section>"
    When click on send button in "<section>"
#    Then text "Thank you for your message" is displayed
    Then email with "generated_test_automation_email_leave_order_emk" contains "+70000000000;Тема: Request from test_automation_company_name" in 900 sec

    Examples:
      | button                           | section                      |
      | leave request button             | request dialog section       |
      | middle request a callback button | request dialog section       |
      | price button                     | request price dialog section |
      | order calculation button         | request dialog section       |
      | send a message button            | request dialog section       |

  Scenario: emkworld.com contacts
    Given open emkworld.com page
    When enter "generated_test_automation_email_cont" in name field in "contact section"
    When enter "test_automation_company_name" in company name field in "contact section"
    When enter "+70000000000" in phone field in "contact section"
    When click on call me button in "contact section"
#    Then text "Thank you for your message" is displayed
    Then email with "generated_test_automation_email_cont" contains "+70000000000;Тема: Request from test_automation_company_name;Please, call me back +70000000000" in 900 sec

