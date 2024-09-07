import os

import dotenv
import pytest

from selectel_tests.models.api_session import session


@pytest.fixture(scope='session', autouse=True)
def load_env():
    dotenv.load_dotenv()


@pytest.fixture(scope='session')
def api_session():
    session.base_url = 'https://api.selectel.ru/'
    session.auth_headers = {os.getenv('token_name'): os.getenv('token_value')}
    return session
