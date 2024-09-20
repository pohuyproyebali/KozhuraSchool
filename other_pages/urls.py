from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ApplicationFromEmployerViewSet

app_name = 'other_page_api'
router = DefaultRouter()

router.register(r'applications_from_employer', ApplicationFromEmployerViewSet, basename='applications_from_employer')
urlpatterns = [
    path('', include(router.urls)),
]