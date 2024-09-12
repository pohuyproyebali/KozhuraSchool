
from rest_framework.routers import DefaultRouter

from courses.models import Company
from courses.views import CourseViewSet, CompanyViewSet, UserViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'company', CompanyViewSet, basename='company')
router.register(r'user', UserViewSet, basename='user')
urlpatterns = router.urls