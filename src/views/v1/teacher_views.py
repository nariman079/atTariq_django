from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from src.models import Discipline, Teacher
from src.serializers.teacher_serializers import (TeacherListSerializer,
                                                 DisciplineListSerializer)


class DisciplineViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = Discipline.objects.all()
    serializer_class = DisciplineListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['priority']
    search_fields = ['title', 'description']
    ordering_fields = ['priority', 'title']


class TeacherViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'head', 'options']
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['gender', 'experience', 'is_main']
    search_fields = ['name', 'surname', 'about']
    ordering_fields = ['name', 'surname', 'experience']



