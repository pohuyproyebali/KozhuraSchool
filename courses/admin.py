from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


from .admin_in_lines.user import UsersToGroupInline, CourseUserGroupInline
from .models import *

from .admin_in_lines.course import *
from .admin_in_lines.lesson import *

# Register your models here.

admin.site.register(Company)
#admin.site.register(User)
admin.site.register(Speaker)


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    inlines = [
        UsersToGroupInline,
    ]


@admin.register(UserGroup)
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_courses')
    search_fields = (
        'name',
        'users__username',
        'users__first_name',
        'users__last_name',
        'users__email',
        'courses__name',
    )
    list_filter = ('users', 'courses')

    def get_courses(self, obj):
        return ', '.join(obj.courses.all().values_list('name', flat=True))
    inlines = [
        CourseUserGroupInline
    ]


@admin.register(LessonToUser)
class LessonToUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson',)
    search_fields = ('user__username', 'lesson__name', 'lesson__program_unit__name')
    list_filter = ('lesson__program_unit__course', 'lesson__name', 'user')


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
            {'fields': [('name', 'company'),
                        ('code_name', 'pdf_link'),
                        'user_groups'], }
        ),
        (
            "Дополнительные настройки",
            {
                'fields': [('skills', 'about', 'about_on_library'), ('preview_image', 'image')],
                'classes': ('collapse',)
            },
        )
    )

    list_filter = ('company__name', 'speakers__speaker__name')
    search_fields = ('name', 'company__name', 'speakers__speaker__name')

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
    field = [('name', 'program_unit')]
    list_display = ('name', 'program_unit')
    list_filter = ('name', 'program_unit__course')
    inlines = [
        VideoToLessonInline,
        SpeakerToLessonInline,
        TextToLessonInline,
        UsersToLessonInline
    ]
