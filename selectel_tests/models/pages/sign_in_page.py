import allure
from selene import browser, have

from selectel_tests.data.user import UserSignIn


class SignInPage:
    def open(self):
        with allure.step('Open "sign in" form'):
            browser.open('/')
            browser.element('.header-main__control').element('a[href*="login"]').click()
            browser.switch_to_next_tab()

    def enter_username(self, value):
        browser.element('#username').type(value)

    def enter_password(self, value):
        browser.element('#current-password').type(value)

    def submit(self):
        browser.element('#login-form').element('.sui-form_submit-button').click()

    def fill_form(self, user: UserSignIn):
        with allure.step('Fill "sign in" form'):
            self.enter_username(user.account_number)
            self.enter_password(user.password)
            self.submit()

    def should_have_alert_message(self):
        with allure.step('Check form results'):
            browser.element('.ant-alert-message').should(have.exact_text(
                'Неверный номер аккаунта или пароль. Если вы регистрировались по приглашению, отметьте чекбокс под полем «номер аккаунта».'))

    def should_have_user_account_number_on_main_page(self, value):
        with allure.step('Check form results'):
            browser.element('.header__control .account-info__id.small').should(have.exact_text(f'Аккаунт {value}'))

    def should_have_message_with_special_code(self):
        with allure.step('Check form results'):
            browser.element('[name=verify_sms_form]').element('.ant-form-item-label').should(
                have.exact_text('Код из СМС'))
