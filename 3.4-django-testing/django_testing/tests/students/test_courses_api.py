import pytest
from model_bakery import baker
from rest_framework.test import APIClient


from students.models import Course


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
    response = client.get('/api/v1/courses/', {'name': 'Jessy'})
    assert response.status_code == 200
