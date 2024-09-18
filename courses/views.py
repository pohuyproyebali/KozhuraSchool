from rest_framework.decorators import action, api_view

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from courses.models import Course, Company, User, CourseToUser, Lesson, LessonToUser, Speaker
from courses.serializers import CourseSerializer, CompanySerializer, UserSerializer, LessonToUserSerializer, \
    SpeakerSerializer


# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    """ Viewset для просмотра и редактирования курсов.  """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LessonToUserViewSet(viewsets.ModelViewSet):
    """ Viewset для просмотра и редактирования курсов.  """
    queryset = LessonToUser.objects.all()
    serializer_class = LessonToUserSerializer


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


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """ Viewset для просмотра пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

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


class SpeakerViewSet(viewsets.ModelViewSet):
    """ ViewSet для просмотра спикеров """
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

