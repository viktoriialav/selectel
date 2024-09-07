from allure import step
from selene import browser

from selectel_tests.data.user import user_for_sign_in_without_two_step_authentication
from selectel_tests.models.applications import app


def test_authorization(api_session):
    user = user_for_sign_in_without_two_step_authentication
    referrer_url = 'https://selectel.ru/'

    with step('Login with API'):
        response = api_session.request(method='POST',
                                       endpoint='v1/login',
                                       data={'login': user.account_number,
                                             'password': user.password,
                                             'referrer_url': referrer_url})

        assert response.status_code == 201

    with step('Get cookies from API'):
        cookie_1 = response.cookies.get('sid')
        cookie_2 = response.cookies.get('uid')

    with step('Set cookie from API'):
        browser.open('https://my.selectel.ru/')
        browser.driver.add_cookie(
            {'name': 'sid', 'value': cookie_1, 'path': '/', 'secure': True, 'sameSite': 'Lax', 'httpOnly': True,
             'domain': 'selectel.ru'})
        browser.driver.add_cookie(
            {'name': 'uid', 'value': cookie_2, 'path': '/', 'secure': True, 'sameSite': 'Lax', 'httpOnly': True,
             'domain': 'selectel.ru'})
        browser.open(referrer_url)

    with step("Verify successful authorization"):
        app.sign_in_page.should_have_user_account_number_on_main_page(user.account_number)
