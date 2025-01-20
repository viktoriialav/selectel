import allure
from selene import browser, have


class MainPageSearch:
    def open(self):
        with allure.step('Open the search on the main page'):
            browser.open('/')
            browser.element('.main-nav__list-search .global-search__btn').with_(timeout=15).click()

    def enter_request(self, value):
        with allure.step('Enter a query in the search box'):
            browser.element('.main-nav .global-search__input input').type(value).press_enter()

    def should_have_special_result(self, value):
        with allure.step('Check the right output of the search'):
            browser.all('.gsc-thumbnail-inside a.gs-title').first.should(have.exact_text(value))

    def should_have_allert_message(self, value):
        with allure.step('Check the right output of the search'):
            browser.element('.gs-no-results-result').should(have.exact_text(value))
