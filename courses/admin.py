from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Speaker)
admin.site.register(Lesson)
admin.site.register(VideoToLesson)
admin.site.register(ImageToTextLesson)
admin.site.register(LessonToUser)
admin.site.register(TextToLesson)
admin.site.register(AnswerToText)


class SpeakerToCourseInline(admin.StackedInline):
    model = SpeakerToCourse
    classes = ['collapse']
    verbose_name = 'Спикеры данного курса'
    extra = 1


class SkillToCourseInline(admin.StackedInline):
    model = Skill
    classes = ['collapse']
    verbose_name = 'Навыки получаемые на этом курсе'


class LessonToCourseInline(admin.StackedInline):
    model = Lesson
    classes = ['collapse']
    verbose_name = 'Уроки данного курса'
    extra = 1


class UserToCourseInline(admin.StackedInline):
    model = CourseToUser
    classes = ['collapse']
    verbose_name = 'Ученики данного курса'
    extra = 1


class ProgramUnitToCourseInline(admin.StackedInline):
    model = ProgramUnit
    classes = ['collapse']
    verbose_name = 'Этапы курса'
    extra = 1


class AboutCourseToCourseInline(admin.StackedInline):
    model = AboutCourse
    classes = ['collapse']
    verbose_name = 'Блоки информации о курсе'
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'company',
        'skills',

        'speakers',
    )
    fieldsets = (
        (
            None,
            {'fields': [('name', 'company')], }
        ),
        (
            "Дополнительные настройки",
            {
                'fields': [('skills', 'about'), ('preview_image', 'image')],
                'classes': ('collapse',)
            },
        )
    )

    inlines = [
        SpeakerToCourseInline,
        UserToCourseInline,
        ProgramUnitToCourseInline,
        AboutCourseToCourseInline,
        SkillToCourseInline
    ]

    def speakers(self, obj):
        return ', '.join(speaker.name for speaker in obj.speakers.all())





