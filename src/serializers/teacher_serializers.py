
from rest_framework import serializers
from src.serializers.base_serializers import TeacherSerializer


class TeacherListSerializer(TeacherSerializer):
    disciplines = serializers.ListSerializer(
        child=serializers.CharField(
            source='title',
        ),
        many=True
    )
