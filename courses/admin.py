from django.contrib import admin
from .models import *

from .admin_in_lines.course import *
from .admin_in_lines.lesson import *

# Register your models here.

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Speaker)
admin.site.register(VideoToLesson)
admin.site.register(ImageToTextLesson)
admin.site.register(LessonToUser)
admin.site.register(TextToLesson)
admin.site.register(AnswerToText)


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

    list_filter = ('name', 'company', 'speakers')

    inlines = [
        SpeakerToCourseInline,
        UserToCourseInline,
        ProgramUnitToCourseInline,
        AboutCourseToCourseInline,
        SkillToCourseInline
    ]

    def speakers(self, obj):
        return ', '.join(speaker.speaker.name for speaker in obj.speakers.all())


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    field = [('name', 'course')]
    list_display = ('name', 'course')
    list_filter = ('name', 'course')
    inlines = [
        VideoToLessonInline,
        SpeakerToLessonInline,
        TextToLessonInline,
        UsersToLessonInline
    ]




