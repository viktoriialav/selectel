import allure
from allure_commons.types import Severity
from selene import browser, have

from selectel_tests.applications import app
from selectel_tests.data.user import user_for_sign_in_without_phone_number, user_for_sign_in_with_wrong_password, \
    user_for_sign_in_with_phone_number


@allure.feature('"Sing in" form')
@allure.title('Test of "sing in" form with right data (without specifying a phone number in the account)')
@allure.tag('Sign in', 'Main page')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_sing_in_to_account_without_phone_number():
    # GIVEN
    with allure.step('Open "sign in" form and create user'):
        app.sign_in_page.open()
        user = user_for_sign_in_without_phone_number

    # WHEN
    with allure.step('Fill registration form'):
        app.sign_in_page.enter_username(user.account_number)
        app.sign_in_page.enter_password(user.password)
        app.sign_in_page.submit()

    # THEN
    with allure.step('Check form results'):
        app.sign_in_page.should_have_user_account_number(user.account_number)


@allure.feature('"Sing in" form')
@allure.title('Test of "sing in" form with wrong password')
@allure.tag('Sign in', 'Main page', 'Wrong password')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_sing_in_to_account_with_wrong_password():
    # GIVEN
    with allure.step('Open "sign in" form and create user'):
        app.sign_in_page.open()
        user = user_for_sign_in_with_wrong_password

    # WHEN
    with allure.step('Fill registration form'):
        app.sign_in_page.enter_username(user.account_number)
        app.sign_in_page.enter_password(user.password)
        app.sign_in_page.submit()

    # THEN
    with allure.step('Check form results'):
        app.sign_in_page.should_have_alert_message()


@allure.feature('"Sing in" form')
@allure.title('Test of "sing in" form with right data (with specifying a phone number in the account)')
@allure.tag('Sign in', 'Main page')
@allure.severity(severity_level=Severity.BLOCKER)
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
def test_sing_in_to_account_with_phone_number():
    # GIVEN
    with allure.step('Open "sign in" form and create user'):
        app.sign_in_page.open()
        user = user_for_sign_in_with_phone_number

    # WHEN
    with allure.step('Fill registration form'):
        app.sign_in_page.enter_username(user.account_number)
        app.sign_in_page.enter_password(user.password)
        app.sign_in_page.submit()

    # THEN
    with allure.step('Check form results'):
        app.sign_in_page.should_have_message_with_special_code()


