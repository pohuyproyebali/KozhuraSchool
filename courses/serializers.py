from django.contrib.auth import get_user_model
from rest_framework import serializers

from courses.models import Course, Company, LessonToUser, Lesson, Speaker, SpeakerToCourse, UserGroup

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


User = get_user_model()


class UserCreateSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            'email',
            'username',
            'password',
            'phone',
        )


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели курсов """
    speakers = serializers.SerializerMethodField(method_name='get_speakers')
    program_units = serializers.SerializerMethodField(method_name='get_program_units')
    about_block = serializers.SerializerMethodField(method_name='get_about_block')
    skills_from_process = serializers.SerializerMethodField(method_name='get_skills_from_process')

    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'code_name',
            'company',
            'about',
            'about_on_library',
            'skills',
            'speakers',
            'program_units',
            'about_block',
            'skills_from_process',
            'image',
            'pdf_link'
        ]
        depth = 4
        read_only_fields = ('id',)

    def get_speakers(self, obj):
        return Course.course_manager.speaker_of_this_course(obj.speakers.all())

    def get_program_units(self, obj):
        return Course.course_manager.program_units_of_this_course(obj.program_units.all())

    def get_about_block(self, obj):
        return Course.course_manager.about_block_of_this_course(obj.about_block.all())

    def get_skills_from_process(self, obj):
        return Course.course_manager.skills_from_process_of_this_course(obj.skills_from_process.all())


class CompanySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели компаний """

    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'video_link',
            'main_text',
            'secondary_text',
            'logo',
            'courses'
        ]
        depth = 1
        read_only_fields = ('id',)


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели пользователя """

    class Meta:
        model = User
        fields = '__all__'
        depth = 2
        read_only_fields = ('id',)
        ref_name = 'my_user'

    def get_groups(self, obj):
        return User.user_manager.available_courses(obj.groups.all())


class UserActualGroupSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели UserGroup """
    class Meta:
        model = UserGroup
        fields = [
            'name',
            'courses',
        ]
        depth = 0

class LessonSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели уроков """

    class Meta:
        model = Lesson
        fields = '__all__'
        depth = 2


class LessonToUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели уроков к пользователям """

    class Meta:
        model = LessonToUser
        fields = '__all__'
        depth = 2


class SpeakerSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели спикеров """

    class Meta:
        model = Speaker
        fields = '__all__'
        depth = 2


class LessonWithQuestionSerializer(serializers.ModelSerializer):
    """ Сериализатор для уроков с вопросами """
    text_to_lesson = serializers.SerializerMethodField(method_name='get_text_to_lesson')
    video_to_lesson = serializers.SerializerMethodField(method_name='get_video_to_lesson')

    class Meta:
        model = Lesson
        fields = [
            'id',
            'name',
            'text_to_lesson',
            'video_to_lesson',
        ]
        depth = 4

    def get_text_to_lesson(self, obj):
        return Lesson.lesson_manager.text_of_this_lesson(obj.text_to_lesson.all())

    def get_video_to_lesson(self, obj):
        return Lesson.lesson_manager.video_link_to_this_lesson(obj.video_to_lesson.all())
