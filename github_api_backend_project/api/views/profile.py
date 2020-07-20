import json

from django.http import JsonResponse
from rest_framework.views import APIView

from ..handlers.github_api_endpoints import GitHubAPI


class Info(APIView):
    def get(self, request, username=None):
        result = GitHubAPI().UseOath(request.auth).get_user_info(username)
        return result

    def patch(self, request):
        data = request.data
        result = GitHubAPI().UseOath(request.auth).patch_user_info(data)
        return result


class Visibility(APIView):
    def get(self, request):
        emails = self._get_emails()
        primary_email = emails[0]
        is_visible = self._is_visible(primary_email)

        return JsonResponse({'is_visible': is_visible})

    def post(self, request):
        is_visible = request.data.get('is_visible', False)
        result = GitHubAPI().UseOath(request.auth).set_user_email_visibility(is_visible)
        return result

    def _get_emails(self) -> list:
        result = GitHubAPI().UseOath(self.request.auth).get_user_emails()
        return json.loads(result.content)

    @staticmethod
    def _is_visible(primary_email) -> bool:
        visibility_map = {
            'private': False,
            'public': True
        }
        visibility = primary_email.get('visibility', False)
        return visibility_map.get(visibility, False)


class Availability(APIView):
    def post(self, request):
        # can't find rest api for such option, only web version
        return NotImplementedError()


class Remove(APIView):
    def delete(self, request):
        return NotImplementedError()

