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

