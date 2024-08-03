import allure
from allure_commons.types import Severity

from selectel_tests.applications import app
from selectel_tests.data.text import text_for_positive_search, text_for_negative_search


@allure.feature('Search on the main page')
@allure.title('Test of search with positive result')
@allure.tag('Search', 'Main page')
@allure.severity(severity_level=Severity.NORMAL)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_main_page_search_positive_result():
    # GIVEN
    with allure.step('Open the search on the main page and define the text'):
        app.main_page_search.open()
        text = text_for_positive_search

    # WHEN
    with allure.step('Enter a query in the search box'):
        app.main_page_search.enter_request(text.input)

    # THEN
    with allure.step('Check the right output of the search'):
        app.main_page_search.should_have_special_result(text.output)


@allure.feature('Search on the main page')
@allure.title('Test of search with positive result')
@allure.tag('Search', 'Main page')
@allure.severity(severity_level=Severity.NORMAL)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_main_page_search_negative_result():
    # GIVEN
    with allure.step('Open the search on the main page and define the text'):
        app.main_page_search.open()
        text = text_for_negative_search

    # WHEN
    with allure.step(''):
        app.main_page_search.enter_request(text.input)

    # THEN
    with allure.step('Check the right output of the search'):
        app.main_page_search.should_have_allert_message(text.output)
