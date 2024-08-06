import allure
from selene import browser, have, command

from selectel_tests.data.service import Service


class PriceCalculator:
    def open(self):
        browser.open('/')
        browser.element('[data-qa=main-nav__link-prices]').click()
        browser.element('.ant-notification-notice-close').click()

    def add_some_services(self, items):
        for item in items:
            if item.name not in {Service.cloud_servers.name, Service.dedicated_servers.name,
                                 Service.dedicated_server_config.name, Service.firewalls.name}:
                with allure.step(f'Add "{item.value}"'):
                    browser.all('.hyper-calc-layout__tab').element_by(have.exact_text(item.value)).click()

    def delete_all_services(self, items):
        for item in items:
            if item.name != Service.dedicated_server_config.name:
                with allure.step(f'Delete "{item.value}"'):
                    browser.all('.single-summary-card__title').element_by(have.exact_text(f'{item.value}')).click()
                    browser.all('.single-summary-card__title').element_by(have.exact_text(f'{item.value}')).element(
                        '.delete-button__icon').click()

    def add_firewall(self, value):
        browser.all('.hyper-calc-layout__tab').element_by(have.exact_text(value)).click()
        browser.all('.firewall-card').first.element('.ant-btn').click()
        browser.all('.add-modal .ant-btn').second.perform(command.js.click)

    def add_dedicated_server(self, value):
        browser.all('.hyper-calc-layout__tab').element_by(have.exact_text(value)).click()
        browser.all('.server--hc').first.element('.ant-btn').click()
        browser.element('.add-modal .ant-btn').perform(command.js.click)

    def should_have_special_button(self):
        browser.element('.hyper-calc-layout .btn--dark').should(have.exact_text('Начать расчет'))
