from unittest import TestCase
from django.http import HttpResponse
from datetime import datetime


class TestView(TestCase):
    def test_current_time(self):
        current_time = datetime.now().time()
        msg = f'Текущее время: {current_time}'
        self.assertEqual(HttpResponse(msg).status_code, 200)
