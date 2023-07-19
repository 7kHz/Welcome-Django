from unittest import TestCase
from rest_framework.test import APIClient
from datetime import datetime


class TestTime(TestCase):
    def test_current_time(self):
        url = '/current_time/'
        client = APIClient()
        response = client.get(url)
        current_time = datetime.now().time()
        msg = f'Текущее время: {current_time}'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, msg)
