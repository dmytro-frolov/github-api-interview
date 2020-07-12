from urllib.parse import urlencode

import requests
from django.conf import settings as cfg
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class Authenticate(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        return redirect(f'{cfg.GITHUB_APP_AUTH_URL}?client_id={cfg.GITHUB_APP_CLIENT_ID}')


class OathCallback(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        code = request.query_params['code']

        r = requests.post(
            cfg.GITHUB_WEB_OATH_URL,
            json={'client_id': cfg.GITHUB_APP_CLIENT_ID,
                  'client_secret': cfg.GITHUB_APP_CLIENT_SECRET,
                  'code': code},
            headers={'Accept': 'application/json'})

        response = r.json()
        access_token = response['access_token']
        refresh_token = response['refresh_token']

        args = urlencode({'access_token': access_token, 'refresh_token': refresh_token})
        return redirect(f'{cfg.FRONTEND_LOGIN_CALLBACK_URL}?{args}')
