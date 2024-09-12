from symtable import Class


from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from courses.models import Course, Company, User, CourseToUser
from courses.serializers import CourseSerializer, CompanySerializer, UserSerializer


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    """ Viewset для просмотра и редактирования курсов.  """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CompanyViewSet(viewsets.ModelViewSet):
    """ Viewset для просмотра компаний """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    @action(detail=True)
    def courses(self, request, pk=None):
        courses = Course.objects.filter(company=pk)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """ Viewset для просмотра пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #@action(detail=True)
    #def user_courses(self, request, pk=None):
    #    courses = [
    #        Course.objects.filter(id=course_to_user.course.id) for course_to_user in CourseToUser.objects.filter(user=pk)
    #    ]
    #    serializer = CourseSerializer(courses[0].union(courses[1:-1]), many=True)
   #     return Response(serializer.data)
    #def academic_performance(self, request, pk=None):
