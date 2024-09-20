from rest_framework import serializers

from other_pages.models import ApplicationFromEmployer


class ApplicationFromEmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationFromEmployer
        fields = '__all__'
        depth = 1

