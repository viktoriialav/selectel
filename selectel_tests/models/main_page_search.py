from selene import browser, have


class MainPageSearch:
    def open(self):
        browser.open('/')
        browser.element('.global-search').click()

    def enter_request(self, value):
        browser.element('.ant-input-search-enter-button .ant-input').type(value).press_enter()

    def should_have_special_result(self, value):
        browser.all('.gs-webResult.gs-result .gs-title').first.should(have.exact_text(value))

    def should_have_allert_message(self, value):
        browser.element('.gs-result.gs-no-results-result').should(have.exact_text(value))

