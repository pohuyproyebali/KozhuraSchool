
from rest_framework.routers import DefaultRouter

from courses.models import Company
from courses.views import CourseViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'company', CompanyViewSet, basename='company')
urlpatterns = router.urls