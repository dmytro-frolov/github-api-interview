import json

import requests
import requests_mock

from django.test import TestCase
from unittest.mock import patch

from ..helpers import logged, to_json_resp


class HelpersTest(TestCase):
    def test_logged(self):
        decorator = logged(lambda f: f)
        decorator(lambda: None)

        self.assertEquals(decorator.__name__, 'with_logging')

    @requests_mock.Mocker()
    def test_to_json_resp(self, f_req):
        expected_json = {"foo": "bar"}
        url = 'http://api.example.com'

        f_req.get(url, json=expected_json)

        decorator = to_json_resp(lambda f: f)
        result = decorator(requests.get(url))

        self.assertEquals(result.content.decode(), json.dumps(expected_json))

    @requests_mock.Mocker()
    def test_to_json_resp_error(self, f_req):
        url = 'http://api.example.com'

        f_req.get(url, text='not json')

        decorator = to_json_resp(lambda f: f)
        result = decorator(requests.get(url))

        self.assertEquals(result.status_code, 400)
