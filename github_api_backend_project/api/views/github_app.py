import logging
from urllib.parse import urlencode

import requests
from django.conf import settings as cfg
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

log = logging.getLogger(__name__)


class Authenticate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        # Endpoints(None).generate_jwt()
        return redirect(f'{cfg.GITHUB_APP_AUTH_URL}?client_id={cfg.GITHUB_APP_CLIENT_ID}')


class OathCallback(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        """
        Callback from github with code parameter for auth an app
        note: refresh tokens could be disabled on github's side
        """
        code = request.query_params['code']
        json_resp = self._authorize(code)

        access_token = json_resp.get('access_token')
        refresh_token = json_resp.get('refresh_token')
        if not access_token:
            log.error(json_resp)
            return JsonResponse({'error': "couldn't get the access token"}, status=400)

        args = urlencode({'access_token': access_token, 'refresh_token': refresh_token})
        return redirect(f'{cfg.FRONTEND_LOGIN_CALLBACK_URL}?{args}')

    @staticmethod
    def _authorize(code):
        r = requests.post(
            cfg.GITHUB_WEB_OATH_URL,
            json={'client_id': cfg.GITHUB_APP_CLIENT_ID,
                  'client_secret': cfg.GITHUB_APP_CLIENT_SECRET,
                  'code': code},
            headers={'Accept': 'application/json'})

        return r.json()

    @staticmethod
    def _are_tokens_present(input_json):
        return input_json.get('access_token') or input_json.get('refresh_token')
