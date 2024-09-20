from django.shortcuts import render
from rest_framework import viewsets

from other_pages.models import ApplicationFromEmployer
from other_pages.serializers import ApplicationFromEmployerSerializer


# Create your views here.

class ApplicationFromEmployerViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing applications from employers"""
    queryset = ApplicationFromEmployer.objects.all()
    serializer_class = ApplicationFromEmployerSerializer
