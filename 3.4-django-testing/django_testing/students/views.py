from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.test import APIClient


from students.filters import CourseFilter
from students.models import Course, Student
from students.serializers import CourseSerializer, StudentSerializer


class CoursesViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CourseFilter


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def get_courses(request):
    client = APIClient()
    response = request.GET.get('/api/v1/courses/', {'name': 'Philosophy'})
    data = response.json()
    context = {'data': data}
    return render(request, 'django_testing/templates/get_courses.html', context)
