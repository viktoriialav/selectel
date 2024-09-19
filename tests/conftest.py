import os

import dotenv
import pytest
from selene import browser
from selenium import webdriver

import config
from selectel_tests.models.api_session import session
from selectel_tests.utils import attach_log


@pytest.fixture(scope='function')
def browser_management():
    driver_options = config.settings.driver_options

    browser.config.base_url = config.settings.base_url
    browser.config.window_width = config.settings.window_width
    browser.config.window_height = config.settings.window_height
    browser.config.driver_name = config.settings.driver_name

    if config.settings.env_context == 'selenoid':

        driver = webdriver.Remote(
            command_executor=config.settings.remote_url,
            options=driver_options)
        browser.config.driver = driver
    else:
        browser.config.driver_options = driver_options

    yield

    attach_log.add_screenshot(browser)
    if config.settings.driver_name != 'firefox':
        attach_log.add_logs(browser)
    attach_log.add_html(browser)
    attach_log.add_video(browser)

    browser.quit()


@pytest.fixture(scope='session')
def api_session():
    dotenv.load_dotenv()
    session.base_url = 'https://api.selectel.ru/'
    session.auth_headers = {os.getenv('token_name'): os.getenv('token_value')}
    return session
