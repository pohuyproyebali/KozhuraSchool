from django.urls import path, include
from rest_framework.routers import DefaultRouter

from courses.models import Company
from courses.views import CourseViewSet, CompanyViewSet, UserViewSet, register_user

app_name = 'courses_api'
router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('register_user/', register_user, name='register_user'),
    path('', include(router.urls))
]
