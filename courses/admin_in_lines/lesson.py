from django.contrib import admin

from courses.models import LessonToUser, TextToLesson, SpeakerToLesson, VideoToLesson


class UsersToLessonInline(admin.TabularInline):
    model = LessonToUser
    classes = ['collapse']
    verbose_name = 'Ученики прошедшие этот урок'
    extra = 1


class TextToLessonInline(admin.TabularInline):
    model = TextToLesson
    classes = ['collapse']
    verbose_name = 'Текстовые блоки к уроку'
    extra = 1


class SpeakerToLessonInline(admin.TabularInline):
    model = SpeakerToLesson
    classes = ['collapse']
    verbose_name = 'Спикеры урока'
    extra = 1


class VideoToLessonInline(admin.TabularInline):
    model = VideoToLesson
    classes = ['collapse']
    verbose_name = "Видео-блоки"
    extra = 1