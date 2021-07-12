# Created by kardash at 12/19/20
Feature: test
  # Enter feature description here

  @test
  Scenario Outline: create order
    Given обнулить таймер
    When открываю <page_name> страницу
    When считаю время загрузки "home"
    When перехожу на страницу cart
    When считаю время загрузки "cart"
    When перехожу на страницу <bank>
#    When считаю время загрузки "payment_before"
#    When ввожу карту <card>
#    Then проверяю наличие элемента <type>
#    When считаю время загрузки "payment_after"
#    When отсылаю результат в гугл таблицу

    Examples:
      | page_name             | bank          | card      | type            |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
      | fitsbody.life/agpromo | alfabank      | alfa card | 3d secure page  |
