import allure
from allure_commons.types import Severity

from selectel_tests.models.applications import app
from selectel_tests.data.service import Service


@allure.feature('Price calculator page')
@allure.severity(severity_level=Severity.NORMAL)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru/prices/calculator/')
class TestPriceCalculator:

    @allure.tag('Service', 'Price', 'Calculator')
    def test_price_calculator_to_add_and_delete_all_options(self, browser_management):
        # GIVEN
        app.price_calculator.open()

        # WHEN
        app.price_calculator.add_all_services(list(Service))
        app.price_calculator.delete_all_services(list(Service))

        # THEN
        app.price_calculator.should_have_special_button()
