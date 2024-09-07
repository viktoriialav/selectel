import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver

from selectel_tests.utils import attach


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='125.0',
        choices=['125.0', '126.0']
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=False)
def browser_management(request):
    browser.config.base_url = 'https://selectel.ru'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    # driver_options = Options()
    # driver_options.page_load_strategy = 'eager'
    #
    # browser_version = request.config.getoption('--browser_version')
    # selenoid_capabilities = {
    #     "browserName": "chrome",
    #     "browserVersion": browser_version,
    #     "selenoid:options": {
    #         "enableVNC": True,
    #         "enableVideo": True
    #     }
    # }
    # driver_options.capabilities.update(selenoid_capabilities)
    #
    # user_login = os.getenv('SELENOID_LOGIN')
    # user_password = os.getenv('SELENOID_PASSWORD')
    # selenoid_url = os.getenv('SELENOID_URL')
    # driver = webdriver.Remote(
    #     command_executor=f'https://{user_login}:{user_password}@{selenoid_url}/wd/hub',
    #     options=driver_options)
    #
    # browser.config.driver = driver
    #
    # yield browser
    #
    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_html(browser)
    # attach.add_video(browser)
    #
    # browser.quit()
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'

    browser.config.driver_options = driver_options

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()