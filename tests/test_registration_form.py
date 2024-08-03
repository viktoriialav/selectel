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
    with allure.step('Open registration form and create user'):
        app.registration_page.open()
        user = user_for_registration_form

    # WHEN
    with allure.step('Fill registration form'):
        app.registration_page.enter_email(user.email)
        app.registration_page.enter_password(user.password)
        app.registration_page.repeat_password(user.password)
        app.registration_page.permit_to_process_personal_data(user.give_personal_data)
        app.registration_page.permit_to_receive_news(user.receive_news)
        app.registration_page.submit()

    # THEN
    with allure.step('Check form results'):
        app.registration_page.should_have_message_with_email(user.email)


@allure.feature('Registration form')
@allure.title('Test of registration form with wrong data')
@allure.tag('Registration form', 'Main page')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_registration_form_with_wrong_data():
    # GIVEN
    with allure.step('Open registration form and create user'):
        app.registration_page.open()
        user = user_for_registration_form_with_wrong_data

    # WHEN
    with allure.step('Fill registration form'):
        app.registration_page.enter_email(user.email)
        app.registration_page.enter_password(user.password)
        app.registration_page.repeat_password(user.password * 2)
        app.registration_page.permit_to_process_personal_data(user.give_personal_data)
        app.registration_page.permit_to_receive_news(user.receive_news)
        app.registration_page.submit()

    # THEN
    with allure.step('Check form results'):
        app.registration_page.should_have_error_messages()


@allure.feature('Registration form')
@allure.title('Test of registration form with empty fields')
@allure.tag('Registration form', 'Main page')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_registration_form_with_empty_fields():
    # GIVEN
    with allure.step('Open registration form and create user'):
        app.registration_page.open()
        user = user_for_registration_form_with_empty_data

    # WHEN
    with allure.step('Fill registration form'):
        app.registration_page.enter_email(user.email)
        app.registration_page.enter_password(user.password)
        app.registration_page.repeat_password(user.password)
        app.registration_page.permit_to_process_personal_data(user.give_personal_data)
        app.registration_page.permit_to_receive_news(user.receive_news)
        app.registration_page.submit()

    # THEN
    with allure.step('Check form results'):
        app.registration_page.should_have_warning_messages()

