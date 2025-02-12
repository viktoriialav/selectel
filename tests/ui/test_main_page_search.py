import allure
import pytest
from allure_commons.types import Severity

from selectel_tests.data.text import text_for_positive_search, text_for_negative_search
from selectel_tests.models.applications import app


@allure.feature('Search on the main page')
@allure.label('owner', 'Viktoriia Lavrova')
@allure.label('layer', 'ui')
@allure.link('https://selectel.ru')
@pytest.mark.ui
class TestMainSearch:
    @allure.severity(severity_level=Severity.CRITICAL)
    @allure.tag('Search', 'Main page', 'Positive result')
    def test_main_page_search_with_positive_result(self, browser_management):
        # GIVEN
        app.main_page_search.open()
        text = text_for_positive_search

        # WHEN
        app.main_page_search.enter_request(text.input)

        # THEN
        app.main_page_search.should_have_special_result(text.output)

    @allure.severity(severity_level=Severity.NORMAL)
    @allure.tag('Search', 'Main page', 'Negative result')
    def test_main_page_search_with_negative_result(self, browser_management):
        # GIVEN
        app.main_page_search.open()
        text = text_for_negative_search

        # WHEN
        app.main_page_search.enter_request(text.input)

        # THEN
        app.main_page_search.should_have_allert_message(text.output)
