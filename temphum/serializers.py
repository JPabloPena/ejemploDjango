from rest_framework import serializers
from .models import TempHum

class TempHumSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempHum
        fields = ('id', 'type', 'value')