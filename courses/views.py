from django.contrib.auth import get_user_model
from rest_framework.decorators import action, api_view

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from courses.models import Course, Company, Lesson, LessonToUser, Speaker, UserGroup
from courses.serializers import CourseSerializer, CompanySerializer, UserSerializer, LessonToUserSerializer, \
    SpeakerSerializer, LessonSerializer, LessonWithQuestionSerializer, UserActualGroupSerializer

User = get_user_model()


# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):
    """ Viewset для просмотра и редактирования курсов.  """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @action(detail=True)
    def lessons(self, request, pk=None):
        lessons = Lesson.objects.filter(course=pk)
        serializer = LessonWithQuestionSerializer(lessons, many=True)
        return Response(serializer.data)


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
    def user_groups(self, request, pk=None):
        groups = UserGroup.objects.filter(users__id=pk)
        serializer = UserActualGroupSerializer(groups, many=True).data
        return Response(serializer)

    @action(detail=True)
    def user_lessons(self, request, pk=None):
        lessons = Lesson.objects.filter(users_to_lesson__user=pk)
        serializer = LessonSerializer(lessons, many=True).data
        return Response(serializer)


class SpeakerViewSet(viewsets.ModelViewSet):
    """ ViewSet для просмотра спикеров """
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
