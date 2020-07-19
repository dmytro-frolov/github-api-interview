import requests
import requests_mock
from django.test import TestCase

from ..handlers.github_api_endpoints import Endpoints, GitHubAPI


class GitHubAPITest(TestCase):
    def test_oauth(self):
        token = 'bear'
        result_s = GitHubAPI().UseOath(token)

        self.assertEquals(result_s.s.headers['Authorization'], token)

    def test_basic_auth(self):
        user, password = 'root', 'swordfish'
        result_s = GitHubAPI().UseBasicAuth(user, password)

        self.assertEquals(result_s.s.auth[1], password)


class EndpointsTest(TestCase):
    def setUp(self):
        session = requests.Session()
        self.adapter = requests_mock.Adapter()
        session.mount('mock://', self.adapter)

        self.api = Endpoints(session)
        self.api.host = 'mock://test.com'

    def test_get_user_info(self):
        username = 'ghost'
        self.adapter.register_uri('GET', f'{self.api.host}/user', json={})
        self.adapter.register_uri('GET', f'{self.api.host}/users/{username}', json={})

        result = self.api.get_user_info()
        self.assertEquals(result.status_code, 200)

        result = self.api.get_user_info(username)
        self.assertEquals(result.status_code, 200)

    def test_patch_user_info(self):
        self.adapter.register_uri('PATCH', f'{self.api.host}/user', json={})
        result = self.api.patch_user_info({})
        self.assertEquals(result.status_code, 200)

    def test_get_user_emails(self):
        self.adapter.register_uri('GET', f'{self.api.host}/user/emails', json={})
        result = self.api.get_user_emails()
        self.assertEquals(result.status_code, 200)

    def test_set_user_email_visibility(self):
        self.adapter.register_uri('PATCH', f'{self.api.host}/user/email/visibility', json={})
        result = self.api.set_user_email_visibility(is_visible=True)
        self.assertEquals(result.status_code, 200)

