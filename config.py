import os
from typing import Literal, Optional

import dotenv
from pydantic_settings import BaseSettings
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions, FirefoxOptions

from selectel_tests.utils import path

BrowserVersions = Literal['100.0', '113.0', '114.0', '120.0', '121.0', '122.0', '123.0', '124.0', '125.0', '126.0']
EnvContext = Literal['local', 'selenoid']
BrowserType = Literal['chrome', 'firefox']


class Settings(BaseSettings):
    env_context: EnvContext = 'local'

    # General
    base_url: str = 'https://selectel.ru'
    driver_name: BrowserType = 'chrome'
    window_width: int = 1920
    window_height: int = 1080
    headless: bool = False

    # Selenoid browser
    browser_version: Optional[BrowserVersions] = None

    # Remote driver
    remote_url: Optional[str] = None

    @property
    def driver_options(self):
        if self.driver_name == 'chrome':
            options = ChromeOptions()
        else:
            options = FirefoxOptions()

        if self.headless:
            options.add_argument('--headless=new')

        if self.env_context == 'selenoid':
            options = Options()
            selenoid_capabilities = {
                "browserName": self.driver_name,
                "browserVersion": self.browser_version or '125.0',
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True
                }
            }

            options.capabilities.update(selenoid_capabilities)

            dotenv.load_dotenv(path.abs_path_from_root('.env'))
            user_login = os.getenv('SELENOID_LOGIN')
            user_password = os.getenv('SELENOID_PASSWORD')
            selenoid_url = os.getenv('SELENOID_URL')
            self.remote_url = f'https://{user_login}:{user_password}@{selenoid_url}/wd/hub'
        else:
            options.page_load_strategy = 'eager'

        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':
        env = env or cls().env_context
        return cls(_env_file=path.abs_path_from_root(f'.env.{env}'))


settings = Settings.in_context()

