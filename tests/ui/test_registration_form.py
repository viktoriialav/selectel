import allure
import pytest
from allure_commons.types import Severity

from selectel_tests.data.user import user_for_registration_form, user_for_registration_form_with_wrong_data, \
    user_for_registration_form_with_empty_data
from selectel_tests.models.applications import app


@allure.feature('Registration form')
@allure.label('owner', 'Viktoriia Lavrova')
@pytest.mark.ui
class TestRegistrationForm:
    @allure.severity(severity_level=Severity.BLOCKER)
    @allure.tag('Registration')
    def test_registration_form_with_right_data(self, browser_management):
        # GIVEN
        app.registration_page.open()
        user = user_for_registration_form

        # WHEN
        app.registration_page.fill_form(user)

        # THEN
        app.registration_page.should_have_message_with_email(user.email)

    @allure.severity(severity_level=Severity.CRITICAL)
    @allure.tag('Registration', 'Wrong data')
    def test_registration_form_with_wrong_data(self, browser_management):
        # GIVEN
        app.registration_page.open()

        # WHEN
        app.registration_page.fill_form(user_for_registration_form_with_wrong_data)

        # THEN
        app.registration_page.should_have_error_messages()

    @allure.severity(severity_level=Severity.CRITICAL)
    @allure.tag('Registration', 'Empty fields')
    def test_registration_form_with_empty_fields(self, browser_management):
        # GIVEN
        app.registration_page.open()

        # WHEN
        app.registration_page.fill_form(user_for_registration_form_with_empty_data)

        # THEN
        app.registration_page.should_have_warning_messages()
