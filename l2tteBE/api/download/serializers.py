from rest_framework import serializers
from api.download.models import DownloadLinkModel


class DownloadLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownloadLinkModel
        fields = '__all__'
