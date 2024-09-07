import allure
from allure_commons.types import Severity

from selectel_tests.models.applications import app
from selectel_tests.data.user import user_for_registration_form, user_for_registration_form_with_wrong_data, \
    user_for_registration_form_with_empty_data


@allure.feature('Registration form')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.label('owner', 'Viktoriia Lavrova')
class TestRegistrationForm:
    class TestPositive:

        @allure.tag('Registration form', 'Main page')
        def test_registration_form_with_right_data(self, browser_management):
            # GIVEN
            app.registration_page.open()
            user = user_for_registration_form

            # WHEN
            app.registration_page.fill_form(user)

            # THEN
            app.registration_page.should_have_message_with_email(user.email)


        @allure.tag('Registration form', 'Main page', 'Wrong data')
        def test_registration_form_with_wrong_data(self, browser_management):
            # GIVEN
            app.registration_page.open()

            # WHEN
            app.registration_page.fill_form(user_for_registration_form_with_wrong_data)

            # THEN
            app.registration_page.should_have_error_messages()

    class TestNegative:

        @allure.tag('Registration form', 'Main page', 'Empty fields')
        def test_registration_form_with_empty_fields(self, browser_management):
            # GIVEN
            app.registration_page.open()

            # WHEN
            app.registration_page.fill_form(user_for_registration_form_with_empty_data)

            # THEN
            app.registration_page.should_have_warning_messages()

