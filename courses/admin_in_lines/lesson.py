from django.contrib import admin

from courses.models import LessonToUser, TextToLesson, SpeakerToLesson, VideoToLesson, AnswerToText, ImageToTextLesson


class UsersToLessonInline(admin.TabularInline):
    model = LessonToUser
    classes = ['collapse']
    verbose_name_plural = 'Ученики прошедшие этот урок'
    extra = 1


class TextToLessonInline(admin.TabularInline):
    model = TextToLesson
    classes = ['collapse']
    verbose_name_plural = 'Текстовые блоки к уроку'
    extra = 1


class SpeakerToLessonInline(admin.TabularInline):
    model = SpeakerToLesson
    classes = ['collapse']
    verbose_name_plural = 'Спикеры урока'
    extra = 1


class VideoToLessonInline(admin.TabularInline):
    model = VideoToLesson
    classes = ['collapse']
    verbose_name_plural = "Видео-блоки"
    extra = 1


class AnswerToTextInline(admin.StackedInline):
    model = AnswerToText
    classes = ['collapse']
    verbose_name_plural = "Ответы на вопрос"
    extra = 1


class ImageToTextInline(admin.TabularInline):
    model = ImageToTextLesson
    classes = ['collapse']
    verbose_name_plural = "Изображения к тексту"
    extra = 1
