from rest_framework import serializers

from apps.sale_announcement.models import SaleAnnouncementModel


class SaleAnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleAnnouncementModel
        fields = '__all__'
