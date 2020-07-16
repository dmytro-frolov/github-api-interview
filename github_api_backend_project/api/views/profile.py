from django.http import JsonResponse
from rest_framework.views import APIView

from ..handlers.github_api_endpoints import GitHubAPI


class Info(APIView):
    def get(self, request, username=None):
        # result = GitHubAPI().UseOath(request.auth).get_user_info(username)
        # return result
        r = {"login": "tttesttt928", "id": 68234816, "node_id": "MDQ6VXNlcjY4MjM0ODE2", "avatar_url": "https://avatars1.githubusercontent.com/u/68234816?v=4", "gravatar_id": "", "url": "https://api.github.com/users/tttesttt928", "html_url": "https://github.com/tttesttt928", "followers_url": "https://api.github.com/users/tttesttt928/followers", "following_url": "https://api.github.com/users/tttesttt928/following{/other_user}", "gists_url": "https://api.github.com/users/tttesttt928/gists{/gist_id}", "starred_url": "https://api.github.com/users/tttesttt928/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/tttesttt928/subscriptions", "organizations_url": "https://api.github.com/users/tttesttt928/orgs", "repos_url": "https://api.github.com/users/tttesttt928/repos", "events_url": "https://api.github.com/users/tttesttt928/events{/privacy}", "received_events_url": "https://api.github.com/users/tttesttt928/received_events", "type": "User",
             "site_admin": False, "name": None, "company": None, "blog": "", "location": None, "email": None,
             "hireable": None, "bio": None, "twitter_username": None, "public_repos": 0, "public_gists": 0,
             "followers": 0, "following": 0, "created_at": "2020-07-13T13:54:18Z", "updated_at": "2020-07-14T12:05:11Z",
             "plan": {"name": "free", "space": 976562499, "collaborators": 0, "private_repos": 10000}}
        return JsonResponse(r)

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

