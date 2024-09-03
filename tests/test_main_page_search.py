import allure
from allure_commons.types import Severity

from selectel_tests.models.applications import app
from selectel_tests.data.text import text_for_positive_search, text_for_negative_search


@allure.feature('Search on the main page')
@allure.title('Test of search with positive result')
@allure.tag('Search', 'Main page')
@allure.severity(severity_level=Severity.NORMAL)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_main_page_search_positive_result():
    # GIVEN
    app.main_page_search.open()
    text = text_for_positive_search

    # WHEN
    app.main_page_search.enter_request(text.input)

    # THEN
    app.main_page_search.should_have_special_result(text.output)


@allure.feature('Search on the main page')
@allure.title('Test of search with negative result')
@allure.tag('Search', 'Main page')
@allure.severity(severity_level=Severity.NORMAL)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_main_page_search_negative_result():
    # GIVEN
    app.main_page_search.open()
    text = text_for_negative_search

    # WHEN
    app.main_page_search.enter_request(text.input)

    # THEN
    app.main_page_search.should_have_allert_message(text.output)
