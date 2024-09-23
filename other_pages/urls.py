from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'other_page_api'
router = DefaultRouter()

router.register(r'applications_from_employer', ApplicationFromEmployerViewSet, basename='applications_from_employer')
router.register(r'news', NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]