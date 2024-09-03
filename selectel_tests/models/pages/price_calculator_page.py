import allure
from selene import browser, have, command, be

from selectel_tests.data.service import Service


class PriceCalculator:
    def open(self):
        with allure.step('Open price calculator'):
            browser.open('/')
            browser.element('[data-qa=main-nav__link-prices]').click()
            browser.element('.ant-notification-notice-close').click()

    def add_firewall(self, item: Service):
        with allure.step(f'Add "{item.value}"'):
            # Open 'Firewalls'
            browser.all('.hyper-calc-layout__tab').element_by(have.exact_text(item.value)).click()

            # Select necessary option and add it
            browser.all('.firewall-card').first.element('.ant-btn').click()
            browser.all('.add-modal .ant-btn').second.perform(command.js.click)

    def add_dedicated_server(self, item: Service):
        with allure.step(f'Add "{item.value}"'):
            # Open 'Dedicated server'
            browser.all('.hyper-calc-layout__tab').element_by(have.exact_text(item.value)).click()

            # Select necessary option and add it
            browser.all('.server--hc .server__quantity--available').first.element('..').element('.ant-btn').click()
            browser.element('.add-modal .ant-btn').perform(command.js.click)

    def add_dedicated_server_config(self, item: Service):
        with allure.step(f'Add "{item.value}"'):
            # Open 'Dedicated server configuration'
            browser.all('.hyper-calc-layout__tab').element_by(have.exact_text(item.value)).click()

            # Open internal frame
            browser.switch_to.frame(
                browser.element('[src="/custom_calc/?new-design&hypercalc"]').with_(timeout=10).should(
                    be.visible).locate())

            # Open processor's menu and select necessary one
            browser.element('#select_12').with_(timeout=10).should(be.visible).click()
            browser.element('#select_container_13').element('#select_option_14').click()

            # Wait for the option to be added
            browser.element('[name=select_ram0]').with_(timeout=10).should(have.attribute('aria-disabled').value('false'))

            # Exit the frame
            browser.switch_to_previous_tab()

    def add_all_services(self, items: list[Service, ...]):
        with allure.step('Add all services'):

            self.add_dedicated_server(Service.dedicated_servers)
            self.add_dedicated_server_config(Service.dedicated_server_config)

            for item in items:
                if item.name not in {Service.cloud_servers.name, Service.dedicated_servers.name,
                                     Service.dedicated_server_config.name, Service.firewalls.name}:
                    with allure.step(f'Add "{item.value}"'):
                        browser.all('.hyper-calc-layout__tab').element_by(have.exact_text(item.value)).click()

            self.add_firewall(Service.firewalls)

    def delete_all_services(self, items: list[Service, ...]):
        with allure.step('Delete all services'):
            for item in items:
                with allure.step(f'Delete "{item.value}"'):
                    browser.all('.single-summary-card__title').element_by(have.exact_text(f'{item.value}')).click()
                    browser.all('.single-summary-card__title').element_by(have.exact_text(f'{item.value}')).element(
                        '.delete-button__icon').perform(command.js.click)

    def should_have_special_button(self):
        with allure.step('Check the result of all actions'):
            browser.element('.hyper-calc-layout .btn--dark').should(have.exact_text('Начать расчет'))
