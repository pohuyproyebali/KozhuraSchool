from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import UserManager
from django.db import models


class MyUserQueryset(models.QuerySet):

    def available_courses(self, user):
        user_groups = user.groups_to_courses.all()
        courses1 = [group.courses.only('name') for group in user_groups]
        courses = []
        for courses0 in courses1:
            for course in courses0:
                if course in courses:
                    continue
                else:
                    courses.append(course)
        courses = {
            course.name: f'id - {course.id}' for course in courses
        }
        return courses

    def done_lessons(self, user):
        courses = {
            course_key: {
                'result':
                f'''{
                len(user.lesson_to_user.filter(
                    lesson__program_unit__course=course_value.split()[-1]
                ))
                }/{
                sum(
                    [len(unit.lessons.all()) for unit in user.groups_to_courses.filter(
                        courses=course_value.split()[-1]
                    )[0].courses.get(
                        id=course_value.split()[-1]
                    ).program_units.all()]
                )
                }''',
                'id': course_value.split()[-1]
            } for course_key, course_value in self.available_courses(user).items()
        }
        return courses


class MyUserManager(UserManager):
    def get_queryset(self):
        return MyUserQueryset(self.model)

    def available_courses(self, user):
        return self.get_queryset().available_courses(user)

    def done_lessons(self, user):
        return self.get_queryset().done_lessons(user)
