from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(ApplicationFromEmployer)
admin.site.register(InnovationBlock)
admin.site.register(InformationBlock)


class ImageToNewsBlockInline(admin.StackedInline):
    model = NewsImage
    extra = 1
    classes = ('collapse',)


@admin.register(NewsBlock)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'news_content', 'news_date')
    list_filter = ('news_date',)
    fields = ('news_title', 'news_content', 'news_date')
    inlines = [ImageToNewsBlockInline]