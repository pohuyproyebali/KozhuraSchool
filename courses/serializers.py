from rest_framework import serializers

from courses.models import Course, Company, User, LessonToUser, Lesson, Speaker


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели курсов """
    class Meta:
        model = Course
        fields = ['id', 'name', 'company', 'about', 'skills']
        depth = 2
        read_only_fields = ('id',)


class CompanySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели компаний """
    class Meta:
        model = Company
        fields = '__all__'
        depth = 2
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



