from abc import ABC, abstractmethod

from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect
from rest_framework.views import APIView

import requests


class Authenticate(APIView):
    def get(self, request):
        r_url = 'https://github.com/login/oauth/authorize?client_id=Iv1.f38f90547b6950a7'
        return redirect(r_url)


class Catch(APIView): #callback
    def get(self, request):
        code = request.query_params['code']
        client_id = 'Iv1.f38f90547b6950a7'
        client_secret = '86f9b2451de9515ea1463d5ba3307f0d1e69e531'

        r = requests.post(
            'https://github.com/login/oauth/access_token',
            json={'client_id': client_id,
                  'client_secret': client_secret,
                  'code': code},
            headers={'Accept': 'application/json'})

        response = r.json()
        access_token = response['access_token']
        refresh_token = response['refresh_token']

        return JsonResponse({'access': access_token, 'refresh_token': refresh_token})