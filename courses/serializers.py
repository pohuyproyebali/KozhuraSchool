from rest_framework import serializers

from courses.models import Course, Company, User, LessonToUser, Lesson, Speaker, SpeakerToCourse


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели курсов """
    speakers = serializers.SerializerMethodField(method_name='get_speakers')
    program_units = serializers.SerializerMethodField(method_name='get_program_units')
    about_block = serializers.SerializerMethodField(method_name='get_about_block')

    class Meta:
        model = Course
        fields = [
            'id',
            'name',
            'company',
            'about',
            'skills',
            'speakers',
            'program_units',
            'about_block'
        ]
        depth = 4
        read_only_fields = ('id',)

    def get_speakers(self, obj):
        return Course.course_manager.speaker_of_this_course(obj.speakers.all())

    def get_program_units(self, obj):
        return Course.course_manager.program_units_of_this_course(obj.program_units.all())

    def get_about_block(self, obj):
        return Course.course_manager.about_block_of_this_course(obj.about_block.all())


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



