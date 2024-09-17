from rest_framework import serializers

from courses.models import Course, Company, User, LessonToUser


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


class LessonToUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели уроков к пользователям """
    class Meta:
        model = LessonToUser
        fields = '__all__'
        depth = 2
        read_only_fields = ('id',)

