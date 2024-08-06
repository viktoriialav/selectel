import allure
from allure_commons.types import Severity

from selectel_tests.applications import app
from selectel_tests.data.service import Service


@allure.feature('Price calculator page')
@allure.title('Test of addition and deletion of all services')
@allure.tag('Service', 'Price', 'Calculator')
@allure.severity(severity_level=Severity.NORMAL)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru/prices/calculator/')
def test_price_calculator_for_cloud_server_perform_price_report():
    app.price_calculator.open()

    # WHEN
    with allure.step('Add all services'):
        with allure.step(f'Add "{Service.dedicated_servers.value}"'):
            app.price_calculator.add_dedicated_server(Service.dedicated_servers.value)

        app.price_calculator.add_some_services(list(Service))

        with allure.step(f'Add "{Service.firewalls.value}"'):
            app.price_calculator.add_firewall(Service.firewalls.value)

    with allure.step('Delete all services'):
        app.price_calculator.delete_all_services(list(Service))

    # THEN
    with allure.step('Check the result of all actions'):
        app.price_calculator.should_have_special_button()
