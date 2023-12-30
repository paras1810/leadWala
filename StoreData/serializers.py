from rest_framework import serializers
from .models import PrimaryData

class PrimarySerializer(serializers.ModelSerializer):
    #Lead_Status = serializers.ReadOnlyField()

    class Meta:
        model = PrimaryData
        fields = '__all__'
