from selene import browser, have


class SignInPage:
    def open(self):
        browser.open('/')
        browser.element('.header__control').element(
            '[data-ph-event="site_component_header_button-login"]').click()
        browser.switch_to_next_tab()

    def enter_username(self, value):
        browser.element('#username').type(value)

    def enter_password(self, value):
        browser.element('#current-password').type(value)

    def submit(self):
        browser.element('#login-form').element('.sui-form_submit-button').click()

    def should_have_alert_message(self):
        browser.element('.ant-alert-message').should(have.exact_text(
            'Неверный номер аккаунта или пароль. Если вы регистрировались по приглашению, отметьте чекбокс под полем «номер аккаунта».'))

    def should_have_user_account_number(self, value):
        browser.element('.sui-profile-dropdown-account-id').should(have.exact_text(f'Аккаунт {value}'))

    def should_have_message_with_special_code(self):
        browser.element('[name=verify_sms_form]').element('.ant-form-item-label').should(
            have.exact_text('Код из СМС'))
