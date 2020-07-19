from django.test import TestCase

from ..handlers.github_api_connection import Oauth, BasicAuth


class ConnectionAuthTest(TestCase):
    def test_oauth(self):
        bearer = 'bear'

        oauth = Oauth()
        oauth.auth(bearer)
        result_s = oauth.session()

        self.assertEquals(result_s, oauth.s)
        self.assertEquals(Oauth._bearer, bearer)
        self.assertEquals(result_s.headers['Authorization'], bearer)

    def test_basic_auth(self):
        user, password = 'root', 'swordfish'

        basic_auth = BasicAuth()
        basic_auth.auth(user, password)
        result_s = basic_auth.session()

        self.assertEquals(result_s, basic_auth.s)
        self.assertEquals(BasicAuth._user, user)
        self.assertEquals(result_s.auth[1], password)
