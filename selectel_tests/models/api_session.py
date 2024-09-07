from requests import Session


class TestSession(Session):
    def __init__(self, base_url=None, auth_headers=None):
        super().__init__()
        self.base_url = base_url
        self.auth_headers = auth_headers

    def request(self, method, endpoint, headers=None, *args, **kwargs):
        joined_headers = dict(self.auth_headers)
        if headers:
            joined_headers.update(headers)
        joined_url = self.base_url + endpoint
        return super().request(method, url=joined_url, headers=joined_headers, *args, **kwargs)


session = TestSession()
