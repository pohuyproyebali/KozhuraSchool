from django.shortcuts import render
from rest_framework import viewsets

from other_pages.models import *
from other_pages.serializers import ApplicationFromEmployerSerializer, NewsSerializer, InformationSerializer, \
    InnovationSerializer


# Create your views here.

class ApplicationFromEmployerViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing applications from employers"""
    queryset = ApplicationFromEmployer.objects.all()
    serializer_class = ApplicationFromEmployerSerializer


class NewsViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing news"""
    queryset = NewsBlock.objects.all()
    serializer_class = NewsSerializer


class InformationViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing information"""
    queryset = InformationBlock.objects.all()
    serializer_class = InformationSerializer


class InnovationViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing innovations"""
    queryset = InnovationBlock.objects.all()
    serializer_class = InnovationSerializer

