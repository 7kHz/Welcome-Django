import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from django.urls import reverse

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


# @pytest.fixture
# def course_factory():
#     def course(*args, **kwargs):
#         return baker.make(Course, *args, **kwargs)
#     return course


@pytest.mark.django_db
def test_course():
    client = APIClient()
    redirect_url = reverse("courses")
    response = client.get(redirect_url)
    assert response.status_code == 200
    # assert data[0]['name'] == 'Philosophy'
