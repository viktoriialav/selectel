import allure
from selene import browser, have

from selectel_tests.data.user import UserRegForm


class RegistrationPage:
    def open(self):
        with allure.step('Open registration form'):
            browser.open('/')
            browser.element('.header__control').element(
                '[data-ph-event="site_component_header_button-registration"]').click()
            browser.switch_to_next_tab()

    def enter_email(self, value):
        browser.element('#email').type(value)

    def enter_password(self, value):
        browser.element('#new-password').type(value)

    def repeat_password(self, value):
        browser.element('[formcontrolname=confirmPassword]').type(value)

    def permit_to_process_personal_data(self, value):
        if value:
            browser.element('[formcontrolname=dataAgreement]').element('.ant-checkbox').click()

    def permit_to_receive_news(self, value):
        if value:
            browser.element('[formcontrolname=receiveNews]').element('.ant-checkbox').click()

    def submit(self):
        browser.element('.content-section .sui-form_submit-button').click()

    def fill_form(self, user: UserRegForm):
        with allure.step('Fill the registration form'):
            self.enter_email(user.email)
            self.enter_password(user.password)
            self.repeat_password(user.repeat_password)
            self.permit_to_process_personal_data(user.give_personal_data)
            self.permit_to_receive_news(user.receive_news)
            self.submit()

    def should_have_error_messages(self):
        with allure.step('Check form results'):
            browser.element('[stl="registration__email_input__pattern_err"]').should(
                have.exact_text('Неверный формат почты'))
            browser.element('[stl="registration__password_input__pattern_err"]').should(
                have.exact_text('Пароль должен содержать не менее 8 знаков'))
            browser.element('[stl="registration__repeat_pass_input__not_equal_err"]').should(
                have.exact_text('Пароли не совпадают'))

    def should_have_warning_messages(self):
        with allure.step('Check form results'):
            browser.element('[stl="registration__email_input__required_err"]').should(
                have.exact_text('Обязательное поле'))
            browser.element('[stl="registration__password_input__required_err"]').should(
                have.exact_text('Обязательное поле'))
            browser.element('[stl="registration__repeat_pass_input__required_err"]').should(
                have.exact_text('Обязательное поле'))
            browser.all('.ant-form-item-explain-error')[-1].should(have.exact_text('Необходимо отметить чекбокс'))

    def should_have_message_with_email(self, value):
        with allure.step('Check form results'):
            browser.element('.main-column .content-section').element('[stl="registration__confirmation__text"]').should(
                have.text(f'Мы отправили письмо для подтверждения электронной почты на адрес'))
            browser.element('.content-section .t-nowrap').should(have.exact_text(value))
