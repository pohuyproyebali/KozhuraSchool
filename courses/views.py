from symtable import Class

from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response

from courses.models import Course, Company
from courses.serializers import CourseSerializer, CompanySerializer


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