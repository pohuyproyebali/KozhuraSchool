from django.contrib import admin

from courses.models import AboutCourse, ProgramUnit, CourseToUser, Lesson, Skill, SpeakerToCourse


class SpeakerToCourseInline(admin.StackedInline):
    model = SpeakerToCourse
    classes = ['collapse']
    verbose_name_plural = 'Спикеры данного курса'
    extra = 1


class SkillToCourseInline(admin.StackedInline):
    model = Skill
    classes = ['collapse']
    verbose_name_plural = 'Навыки получаемые на этом курсе'


class LessonToCourseInline(admin.StackedInline):
    model = Lesson
    classes = ['collapse']
    verbose_name_plural = 'Уроки данного курса'
    extra = 1


class UserToCourseInline(admin.StackedInline):
    model = CourseToUser
    classes = ['collapse']
    verbose_name_plural = 'Ученики данного курса'
    extra = 1


class ProgramUnitToCourseInline(admin.StackedInline):
    model = ProgramUnit
    classes = ['collapse']
    verbose_name_plural = 'Этапы курса'
    extra = 1


class AboutCourseToCourseInline(admin.StackedInline):
    model = AboutCourse
    classes = ['collapse']
    verbose_name_plural = 'Блоки информации о курсе'
    extra = 1

