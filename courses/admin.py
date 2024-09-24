from django.contrib import admin
from .models import *

from .admin_in_lines.course import *
from .admin_in_lines.lesson import *

# Register your models here.

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Speaker)


@admin.register(LessonToUser)
class LessonToUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson__name', 'lesson__course')
    search_fields = ('user__username', 'lesson__name', 'lesson__course__name')
    list_filter = ('lesson__course', 'lesson', 'user')

@admin.register(TextToLesson)
class TextToLessonAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'name')
    list_filter = ('lesson',)
    search_fields = ('name',)
    inlines = [
        AnswerToTextInline,
        ImageToTextInline
    ]


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
