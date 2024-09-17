import pytest
from selene import browser
from selenium import webdriver

import config
from selectel_tests.utils import attach


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

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
