from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager
from django.db import models


class MyUserQueryset(models.QuerySet):

    def available_courses(self, user):
        user_groups = user.groups_to_courses.all()
        courses1 = [group.courses.only('name') for group in user_groups]
        courses = []
        for course in courses1:
            if course in courses:
                continue
            else:
                courses.append(course)
        return courses


class MyUserManager(UserManager):
    def get_queryset(self):
        return MyUserQueryset(self.model)

    def available_courses(self, user):
        User = get_user_model()
        return self.get_queryset().available_courses(User.objects.get(id=user.id))
