from rest_framework import authentication
from rest_framework import exceptions


class GithubUser:
    is_authenticated = True


class GithubOath(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            raise exceptions.AuthenticationFailed('Token is not provided. Please authorise')

        return GithubUser, auth_header
