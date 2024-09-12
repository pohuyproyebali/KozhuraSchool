from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Course)
admin.site.register(models.Company)
admin.site.register(models.User)
admin.site.register(models.Speaker)
admin.site.register(models.Skill)
admin.site.register(models.Lesson)
admin.site.register(models.VideoToLesson)
admin.site.register(models.ImageToTextLesson)
admin.site.register(models.CourseToUser)
admin.site.register(models.LessonToUser)
admin.site.register(models.TextToLesson)
admin.site.register(models.SpeakerToCourse)
admin.site.register(models.ProgramUnit)
admin.site.register(models.AnswerToText)
admin.site.register(models.AboutCourse)
