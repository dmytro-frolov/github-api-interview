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
        result = GitHubAPI().UseOath(request.auth).get_user_emails()
        return result

    def post(self, request):
        is_visible = request.data.get('isVisible', False)
        result = GitHubAPI().UseOath(request.auth).set_user_email_visibility(is_visible)
        return result


class Availability(APIView):
    def post(self, request):
        # can't find rest api for such option, only web version
        return NotImplementedError()


class Remove(APIView):
    def delete(self, request):
        return NotImplementedError()

