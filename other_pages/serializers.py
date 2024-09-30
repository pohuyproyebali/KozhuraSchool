from rest_framework import serializers

from other_pages.models import *

from KozhuraSchool.settings import IMAGE_SOURCES_DIR


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
        return {IMAGE_SOURCES_DIR + '/' + image['image'] for image in obj.images.all().values('image')}


class InformationSerializer(serializers.ModelSerializer):
    """ Сериализатор для блоков информаации """

    class Meta:
        model = InformationBlock
        fields = '__all__'
        depth = 1


class InnovationSerializer(serializers.ModelSerializer):
    """ Сериализатор для блоков иноваций """

    class Meta:
        model = InnovationBlock
        fields = '__all__'
        depth = 1
