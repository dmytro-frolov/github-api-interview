import time

import jwt
from django.conf import settings

from ..handlers.github_api_connection import Oauth, BasicAuth
from ..helpers import logged, to_json_resp


class Endpoints:
    host = settings.GITHUB_API_URL

    def __init__(self, session):
        self.s = session

    @to_json_resp
    def get_user_info(self, username=None):
        """
        if user not specified return info about current use
        """
        if username is None:
            result = self.s.get(f'{self.host}/user')
        else:
            result = self.s.get(f'{self.host}/users/{username}')

        return result

    @to_json_resp
    def patch_user_info(self, data):
        return self.s.patch(f'{self.host}/user', json=data)

    @to_json_resp
    def get_user_emails(self):
        return self.s.get(f'{self.host}/user/emails')

    @to_json_resp
    def set_user_email_visibility(self, is_visible=False):
        visibility = {
            True: 'public',
            False: 'private'
        }

        return self.s.patch(f'{self.host}/user/email/visibility',
                            json={"email": '',
                            "visibility": visibility[is_visible]})

    def generate_jwt(self):
        from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
        jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))

        # jwt.encode(claim, private_key, algorithm='RS256')

        private_key = settings.GITHUB_APP_PRIVATE_KEY
        # print(private_key)
        # encoded_jwt = jwt.encode({'iss': settings.GITHUB_APP_ID}, private_key, algorithm='RS256')
        #

        now = int(time.time())
        payload = {'iat': now, 'exp': now + 60, 'iss': settings.GITHUB_APP_ID}
        encoded_jwt = jwt.encode(payload, key=private_key, algorithm="RS256")

        print('>>>>>>>', encoded_jwt)
        import requests

        s = requests.session()
        s.headers = {
            "Authorization": f"Bearer {encoded_jwt}",
            "Accept": "application/vnd.github.machine-man-preview+json"
        }
        s.get (self.host+'/app')
        print()


class GitHubAPI:
    @logged
    def UseOath(self, auth_header):
        Oauth().auth(auth_header)
        session = Oauth().session()

        return Endpoints(session)

    @logged
    def UseBasicAuth(self, username, password):
        BasicAuth().auth(username, password)
        session = BasicAuth().session()

        return Endpoints(session)

