from django.conf import settings
from rest_framework import serializers

from src.models import Teacher, Discipline
from src.serializers.base_serializers import (TeacherSerializer,
                                              DisciplineSerializer)


class DisciplineListSerializer(DisciplineSerializer):
    pass


class TeacherDisciplineSerializer(DisciplineSerializer):
    class Meta:
        model = Discipline
        fields = (
            'id',
            'title'
        )


class TeacherListSerializer(TeacherSerializer):
    disciplines = serializers.SerializerMethodField()
    discipline_count = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        exclude = (
            'email',
            'telegram_id',
            'opportunities',
            'study_methods',
            'is_main'
        )

    def get_discipline_count(self, obj: Teacher) -> int:
        return len(obj.disciplines.all()) - settings.DISCIPLINE_COUNT_IN_LIST

    def get_disciplines(self, obj: Teacher) -> any:
        return TeacherDisciplineSerializer(
            instance=obj.disciplines.all()[:settings.DISCIPLINE_COUNT_IN_LIST],
            many=True,
        ).data


