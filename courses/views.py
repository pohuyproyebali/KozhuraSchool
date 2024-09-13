from rest_framework.decorators import action

from rest_framework import viewsets, permissions
from rest_framework.response import Response

from courses.models import Course, Company, User, CourseToUser, Lesson, LessonToUser
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

    @action(detail=True)
    def user_courses(self, request, pk=None):
        courses = [
            Course.objects.filter(id=course_to_user.course.id) for course_to_user in CourseToUser.objects.filter(user=pk)
        ]
        courses_qs = courses[0]
        for course in courses[1:]:
            courses_qs = courses_qs.union(course)

        serializer = CourseSerializer(courses_qs, many=True).data
        response = [
            course.update(
                {
                    'passing percentage': f'{LessonToUser.objects.filter(user=pk, lesson__course=course['id']).count()} / {Lesson.objects.filter(course=course['id']).count()}',
                }
            ) for course in serializer
        ]
        return Response(serializer)

