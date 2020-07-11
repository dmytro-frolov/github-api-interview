from abc import ABC, abstractmethod

import requests


class GitHubSession(ABC):
    """
    Interface provides connection to github.
    :returns requests.session obj
    """
    def __init__(self):
        self.s = requests.session()
        self.s.headers = {
            'User-Agent': 'github-api-backend-project',
            'Accept': 'application/vnd.github.v3+json'
        }

    @classmethod
    @abstractmethod
    def auth(cls, creds):
        pass

    @abstractmethod
    def session(self):
        return requests.session()


class BasicAuth(GitHubSession):
    """
    BasicAuth for github RestAPi
    """
    @classmethod
    def auth(cls, user, password):
        cls._user = user
        cls._password = password

    def session(self):
        self.s.auth = (self._user, self._password)

        return self.s


class Oauth(GitHubSession):
    """
    Oath for github RestApi
    """
    @classmethod
    def auth(cls, auth_header):
        cls._bearer = auth_header

    def session(self):
        self.s.headers.update({'Authorization': self._bearer})

        return self.s
