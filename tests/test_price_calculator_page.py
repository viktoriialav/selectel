import allure
from allure_commons.types import Severity
from selene import browser, have

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

        # TODO Add addition of Service.dedicated_server_config.value

        for item in list(Service):
            if item.name not in {Service.cloud_servers.name, Service.dedicated_servers.name,
                                 Service.dedicated_server_config.name, Service.firewalls.name}:
                with allure.step(f'Add "{item.value}"'):
                    app.price_calculator.add_service(item.value)

        with allure.step(f'Add "{Service.firewalls.value}"'):
            app.price_calculator.add_firewall(Service.firewalls.value)

    with allure.step('Delete all services'):
        for item in list(Service):
            if item.name != Service.dedicated_server_config.name:
                with allure.step(f'Delete "{item.value}"'):
                    app.price_calculator.delete_service(item.value)

    # THEN
    with allure.step('Check the result of all actions'):
        browser.element('.hyper-calc-layout .btn--dark').should(have.exact_text('Начать расчет'))
