from django.contrib import admin

from courses.models import UserGroup, User, Course


class UsersToGroupInline(admin.TabularInline):
    model = UserGroup.users.through
    verbose_name_plural = 'Группы для курсов данного пользователя'
    extra = 1


class CourseUserGroupInline(admin.TabularInline):
    model = Course.user_groups.through
    verbose_name_plural = 'Курсы, доступные данной группе'
    extra = 1
