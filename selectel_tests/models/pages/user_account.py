import allure
from selene import browser, have, query, command, be


class UserAccount:
    def __init__(self):
        self.before_comparison_menu = browser.all('.comparison-popup_buttons .mobile-button-with-stretch')
        self.server_amount = browser.element('.sui-status-color-default')
        self.server_name_list = browser.all('[data-testid=order_list_item_name]')
        self.server_button_list = browser.all('.mobile-button-with-stretch')
        self.account_id = browser.element('.sui-profile-dropdown-account-id')
        self.account_balance = browser.element('[data-testid="value"]')

    def open(self):
        with allure.step('Open the user account'):
            browser.open('/')
            browser.element('.header__control .account-info__id.small').click()
            browser.all('.account-info__dropdown .ant-dropdown-menu-item').element_by(
                have.exact_text('Панель управления')).click()

    def open_server_section(self):
        with allure.step('Open the server section in the user account'):
            browser.all('.ant-menu-title-content').first.click()

    def clear(self):
        with allure.step('Check that the comparison list is clear'):
            self.server_amount.with_(timeout=10).should(be.visible)
            server_amount = self.server_amount.get(query.text)

            if len(self.server_button_list) != int(server_amount.split()[0]):
                with allure.step('Clear the comparison list'):
                    self.before_comparison_menu.element_by(have.exact_text('Очистить')).click()

    def add_in_comparison_first_two_servers(self):
        self.clear()
        with allure.step('Add the first two servers in comparison list'):
            name_list = []
            for i in range(2):
                self.server_name_list[i].with_(timeout=10).perform(command.js.scroll_into_view).should(be.visible)
                name = self.server_name_list[i].get(query.text)
                name_list.append(name)
                self.server_button_list[i].with_(timeout=10).perform(command.js.scroll_into_view).should(be.clickable)
                self.server_button_list[i].perform(command.js.click)
        return name_list

    def go_to_comparison_list(self):
        with allure.step('Go to the comparison list'):
            self.before_comparison_menu.element_by(have.exact_text('Перейти в сравнение')).click()

    def should_have_specific_server_names_in_comparison_list(self, values):
        with allure.step('Check the comparison list'):
            browser.element('.header .ant-typography').should(have.exact_text('Сравнение серверов'))
            browser.all('.sui-typography-high-emphasis.ant-typography').should(have.exact_texts(*values))

    def should_have_user_account_number(self, value):
        with allure.step('Check form results'):
            self.account_id.should(have.exact_text(f'Аккаунт {value}'))

    def should_have_specific_information_in_account(self, account_number, email, balance):
        with allure.step('Check account information'):
            self.account_balance.with_(timeout=10).should(be.visible)
            self.account_id.should(have.exact_text(f'Аккаунт {account_number}'))
            browser.element('.sui-profile-dropdown-account-email').should(have.exact_text(email))
            self.account_balance.should(have.text(balance))
