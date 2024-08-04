from django.contrib import admin
from src.models import Discipline, Statistic, Customer, Teacher


@admin.register(Teacher)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'experience',
    )


@admin.register(Discipline)
class DisciplineModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'priority'
    )


@admin.register(Statistic)
class StatisticModelAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'count'
    )
