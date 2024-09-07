import allure
from allure_commons.types import Severity

from selectel_tests.models.applications import app
from selectel_tests.data.text import text_for_positive_search, text_for_negative_search


@allure.feature('Search on the main page')
@allure.severity(severity_level=Severity.NORMAL)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
class TestMainSearch:
    class TestPositive:
        @allure.tag('Search', 'Main page')
        def test_main_page_search_with_positive_result(self, browser_management):
            # GIVEN
            app.main_page_search.open()
            text = text_for_positive_search

            # WHEN
            app.main_page_search.enter_request(text.input)

            # THEN
            app.main_page_search.should_have_special_result(text.output)

    class TestNegative:
        @allure.tag('Search', 'Main page')
        def test_main_page_search_with_negative_result(self, browser_management):
            # GIVEN
            app.main_page_search.open()
            text = text_for_negative_search

            # WHEN
            app.main_page_search.enter_request(text.input)

            # THEN
            app.main_page_search.should_have_allert_message(text.output)
