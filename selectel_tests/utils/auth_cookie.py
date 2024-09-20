from allure import step
from selene import browser

from selectel_tests.data.user import user_for_sign_in_without_two_step_auth


def get_auth_cookie(api_session):
    user = user_for_sign_in_without_two_step_auth
    referrer_url = 'https://selectel.ru/'

    with step('Login with API'):
        response = api_session.request(method='POST',
                                       endpoint='v1/login',
                                       data={'login': user.account_number,
                                             'password': user.password,
                                             'referrer_url': referrer_url})

    with step('Get cookies from API'):
        cookie_1 = response.cookies.get('sid')
        cookie_2 = response.cookies.get('uid')

    with step('Add authorization cookie'):
        browser.open('/')
        browser.driver.add_cookie(
            {'name': 'sid', 'value': cookie_1, 'path': '/', 'secure': True, 'sameSite': 'Lax', 'httpOnly': True,
             'domain': 'selectel.ru'})
        browser.driver.add_cookie(
            {'name': 'uid', 'value': cookie_2, 'path': '/', 'secure': True, 'sameSite': 'Lax', 'httpOnly': True,
             'domain': 'selectel.ru'})
