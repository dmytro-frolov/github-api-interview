from unittest.mock import patch, Mock

from django.http import JsonResponse
from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate

from ..auth import GithubUser
from ..views.profile import Info, Visibility


class ProfileViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    @patch('api.views.profile.GitHubAPI')
    def test_get_info(self, f_api):
        request = self.factory.get('')
        request.auth = Mock()

        Info().get(request, 'root')

        self.assertTrue(f_api().UseOath().get_user_info.called)

    @patch('api.views.profile.GitHubAPI')
    def test_patch_info(self, f_api):
        f_api().UseOath().patch_user_info = JsonResponse

        request = self.factory.patch('', {"foo": "bar"}, format='json')
        request.auth = Mock()
        force_authenticate(request, user=GithubUser)

        view = Info.as_view()
        response = view(request)

        self.assertEquals(response.status_code, 200)

    @patch('api.views.profile.GitHubAPI')
    def test_get_visibility(self, f_api):
        request = self.factory.get('')
        request.auth = Mock()
        force_authenticate(request, user=GithubUser)

        f_api().UseOath().get_user_emails.return_value = JsonResponse([{"visibility": "public"}],
                                                                      safe=False)

        view = Visibility.as_view()
        response = view(request)

        self.assertEquals(response.content, b'{"is_visible": true}')

    @patch('api.views.profile.GitHubAPI')
    def test_post_visibility(self, f_api):
        request = self.factory.post('', {'is_visible': True}, format='json')
        request.auth = Mock()
        force_authenticate(request, user=GithubUser)
        f_api().UseOath().set_user_email_visibility.return_value = JsonResponse({})

        view = Visibility.as_view()
        response = view(request)
        self.assertEquals(response.status_code, 200)
