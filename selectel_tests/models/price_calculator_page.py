from selene import browser, have


class PriceCalculator:
    def open(self):
        browser.open('/')
        browser.element('[data-qa=main-nav__link-prices]').click()
        browser.element('.ant-notification-notice-close').click()

    def add_service(self, value):
        browser.all('.hyper-calc-layout__tab ').element_by(have.exact_text(value)).click()

    def delete_service(self, value):
        browser.all('.single-summary-card__title').element_by(have.exact_text(f'{value}')).click()
        browser.all('.single-summary-card__title').element_by(have.exact_text(f'{value}')).element(
            '.delete-button__icon').click()

    def add_firewall(self, value):
        browser.all('.hyper-calc-layout__tab ').element_by(have.exact_text(value)).click()
        browser.all('.firewall-card').first.element('.ant-btn').click()
        browser.all('.add-modal .ant-btn').second.click()

    def add_dedicated_server(self, value):
        browser.all('.hyper-calc-layout__tab ').element_by(have.exact_text(value)).click()
        browser.all('.server--hc').first.element('.ant-btn').click()
        browser.element('.add-modal .ant-btn').click()