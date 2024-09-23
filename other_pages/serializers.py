from rest_framework import serializers

from other_pages.models import *


class ApplicationFromEmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationFromEmployer
        fields = '__all__'
        depth = 1


class NewsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_images')

    class Meta:
        model = NewsBlock
        fields = [
            'news_title',
            'news_content',
            'news_date',
            'images'
        ]

    def get_images(self, obj):
        return obj.images.all().values('image')


