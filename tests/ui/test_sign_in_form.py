import allure
from allure_commons.types import Severity

from selectel_tests.models.applications import app
from selectel_tests.data.user import (user_for_sign_in_without_two_step_authentication,
                                      user_for_sign_in_with_wrong_password,
                                      user_for_sign_in_with_two_step_authentication)


@allure.feature('"Sing in" form')
@allure.label('owner', 'Viktoriia Lavrova')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.link('https://selectel.ru')
class TestSignInForm:
    class TestPositive:
        @allure.tag('Sign in', 'Main page')
        def test_sing_in_to_account_without_two_step_authentication(self, browser_management):
            # GIVEN
            app.sign_in_page.open()
            user = user_for_sign_in_without_two_step_authentication

            # WHEN
            app.sign_in_page.fill_form(user)

            # THEN
            app.sign_in_page.should_have_user_account_number(user.account_number)

        @allure.tag('Sign in', 'Main page')
        def test_sing_in_to_account_with_two_step_authentication(self, browser_management):
            # GIVEN
            app.sign_in_page.open()

            # WHEN
            app.sign_in_page.fill_form(user_for_sign_in_with_two_step_authentication)

            # THEN
            app.sign_in_page.should_have_message_with_special_code()

    class TestNegative:
        @allure.tag('Sign in', 'Main page', 'Wrong password')
        def test_sing_in_to_account_with_wrong_password(self, browser_management):
            # GIVEN
            app.sign_in_page.open()

            # WHEN
            app.sign_in_page.fill_form(user_for_sign_in_with_wrong_password)

            # THEN
            app.sign_in_page.should_have_alert_message()





