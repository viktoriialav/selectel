import allure
from allure_commons.types import Severity

from selectel_tests.data.user import user_for_testing_account
from selectel_tests.models.applications import app
from selectel_tests.utils.auth_cookie import get_auth_cookie


@allure.feature('User account')
@allure.label('owner', 'Viktoriia Lavrova')
@allure.link('https://selectel.ru')
class TestUserAccount:
    @allure.severity(severity_level=Severity.CRITICAL)
    @allure.tag('User account', 'Balance', 'Account number', 'Email')
    def test_check_main_info(self, api_session, browser_management):
        # GIVEN
        get_auth_cookie(api_session)
        user = user_for_testing_account
        app.user_account.open()

        # THEN
        app.user_account.should_have_specific_information_in_account(account_number=user.account_number,
                                                                     email=user.email,
                                                                     balance=user.account_balance)

    @allure.severity(severity_level=Severity.NORMAL)
    @allure.tag('User account', 'Dedicated server', 'Comparison')
    def test_add_servers_in_comparison_list(self, api_session, browser_management):
        # GIVEN
        get_auth_cookie(api_session)
        app.user_account.open()
        app.user_account.open_server_section()

        # WHEN
        names = app.user_account.add_in_comparison_first_two_servers()
        app.user_account.go_to_comparison_list()

        # THEN
        app.user_account.should_have_specific_server_names_in_comparison_list(names)
