# Created by Alex Kardash at 24/07/2021
@regression
Feature: Проверка сайта emksteel.ru

  Scenario Outline: emksteel.ru заказать звонок
    Given open emksteel.ru page
    When click on <button>
    When enter "generated_test_automation_email" in name field in "request call section"
    When enter "test_automation_company" in company name field in "request call section"
    When enter "+70000000000" in phone field in "request call section"
    When click on send button in "request call section"
    Then text "Спасибо за Ваше сообщение" is displayed
    Then email with "generated_test_automation_email" contains "Запрос звонка emksteel.ru test_automation_company;Пожалуйста, перезвоните мне;[PHONE]: +7 (000) 000-00-00"" in 240 sec

    Examples:
      | button                     |
      | top request call button    |
      | bottom request call button |
      | request call back button   |

  Scenario: emksteel.ru оставить заявку
    Given open emksteel.ru page
    When enter "generated_test_automation_email" in name field in "1 section"
    When enter "test_automation_company_name" in company name field in "1 section"
    When enter "automation.emk@gmail.com" in email field in "1 section"
    When enter "+70000000000" in phone field in "1 section"
    When enter "test_automation_comment" in message field in "1 section"
    When click on send button in "1 section"
    Then email with "generated_test_automation_email" contains "Тема: Запрос от test_automation_company_name;[PHONE]: +7 (000) 000-00-00;[EMAIL]: automation.emk@gmail.com;[BODY]: test_automation_comment"" in 240 sec


  Scenario Outline: emksteel.ru диалог оставить заявку
    Given open emksteel.ru page
    When enter "test_automation_comment" in message field in "1 section"
    When click on <button>
    When wait 1 sec
    When enter "generated_test_automation_email" in name field in "1 section"
    When enter "test_automation_company_name" in company name field in "1 section"
    When enter "automation.emk@gmail.com" in email field in "1 section"
    When enter "+70000000000" in phone field in "1 section"
    When enter "test_automation_comment" in message field in "1 section"
    When click on send button in "1 section"
    Then email with "generated_test_automation_email" contains "Тема: Запрос от test_automation_company_name;[PHONE]: +7 (000) 000-00-00;[EMAIL]: automation.emk@gmail.com;[BODY]: test_automation_comment"" in 240 sec
    Examples:
      | button            |
      | more info button  |
      | send email button |

  Scenario: emksteel.ru оставить заявку
    Given open emksteel.ru page
    When enter "generated_test_automation_email" in name field in "1 section"
    When enter "test_automation_company_name" in company name field in "1 section"
    When enter "automation.emk@gmail.com" in email field in "1 section"
    When enter "+70000000000" in phone field in "1 section"
    When enter "test_automation_comment" in message field in "1 section"
    When click on send button in "1 section"
    Then email with "generated_test_automation_email" contains "Тема: Запрос от test_automation_company_name;[PHONE]: +7 (000) 000-00-00;[EMAIL]: automation.emk@gmail.com;[BODY]: test_automation_comment"" in 240 sec

#  Scenario: emksteel.ru quiz
#    When download cat image
#    Given open emksteel.ru page
#    When click on price calculation button
#    When open last tab
#    When click on start button
#    When click on black button
#    When click on next button
#    When click on yes checkbox
#    When click on next button
#    When enter "cat.jpg" in file input
#    When click on next button
#    When enter "text_automation_email" in name quiz field
#    When enter "automation.emk@gmail.com" in email quiz field
#    When click on country dropdown
#    When click on russia country
#    When enter "9000000000" in phone quiz field
#    When click on send quiz button
#    Then text "Благодарим за Ваше обращение!" is displayed

