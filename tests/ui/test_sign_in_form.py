import allure
import pytest
from allure_commons.types import Severity

from selectel_tests.data.user import (user_for_sign_in_without_two_step_auth,
                                      user_for_sign_in_with_wrong_password,
                                      user_for_sign_in_with_two_step_auth)
from selectel_tests.models.applications import app


@allure.feature('"Sing in" form')
@allure.label('owner', 'Viktoriia Lavrova')
@allure.label('layer', 'ui')
@allure.link('https://my.selectel.ru/login')
@pytest.mark.ui
class TestSignInForm:
    @allure.severity(severity_level=Severity.BLOCKER)
    @allure.tag('Sign in')
    def test_sign_in_to_account_without_two_step_authentication(self, browser_management):
        # GIVEN
        app.sign_in_page.open()
        user = user_for_sign_in_without_two_step_auth

        # WHEN
        app.sign_in_page.fill_form(user)

        # THEN
        app.user_account.should_have_user_account_number(user.account_number)

    @allure.severity(severity_level=Severity.BLOCKER)
    @allure.tag('Sign in', 'Two-step authentication')
    def test_sign_in_to_account_with_two_step_authentication(self, browser_management):
        # GIVEN
        app.sign_in_page.open()

        # WHEN
        app.sign_in_page.fill_form(user_for_sign_in_with_two_step_auth)

        # THEN
        app.sign_in_page.should_have_message_with_special_code()

    @allure.severity(severity_level=Severity.CRITICAL)
    @allure.tag('Sign in', 'Wrong password')
    def test_sign_in_to_account_with_wrong_password(self, browser_management):
        # GIVEN
        app.sign_in_page.open()

        # WHEN
        app.sign_in_page.fill_form(user_for_sign_in_with_wrong_password)

        # THEN
        app.sign_in_page.should_have_alert_message()
