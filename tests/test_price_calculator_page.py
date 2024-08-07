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
    # GIVEN
    app.price_calculator.open()

    # WHEN
    app.price_calculator.add_all_services(list(Service))
    app.price_calculator.delete_all_services(list(Service))

    # THEN
    app.price_calculator.should_have_special_button()
