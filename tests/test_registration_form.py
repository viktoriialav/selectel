import allure
from allure_commons.types import Severity

from selectel_tests.applications import app
from selectel_tests.data.user import user_for_registration_form, user_for_registration_form_with_wrong_data, \
    user_for_registration_form_with_empty_data


@allure.feature('Registration form')
@allure.title('Test of registration form with right data')
@allure.tag('Registration form', 'Main page')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_registration_form():
    # GIVEN
    app.registration_page.open()
    user = user_for_registration_form

    # WHEN
    app.registration_page.fill_form(user)

    # THEN
    app.registration_page.should_have_message_with_email(user.email)


@allure.feature('Registration form')
@allure.title('Test of registration form with wrong data')
@allure.tag('Registration form', 'Main page')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_registration_form_with_wrong_data():
    # GIVEN
    app.registration_page.open()

    # WHEN
    app.registration_page.fill_form(user_for_registration_form_with_wrong_data)

    # THEN
    app.registration_page.should_have_error_messages()


@allure.feature('Registration form')
@allure.title('Test of registration form with empty fields')
@allure.tag('Registration form', 'Main page')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_registration_form_with_empty_fields():
    # GIVEN
    app.registration_page.open()

    # WHEN
    app.registration_page.fill_form(user_for_registration_form_with_empty_data)

    # THEN
    app.registration_page.should_have_warning_messages()

