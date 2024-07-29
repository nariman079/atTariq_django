from django.db import models


class StatisticType(models.TextChoices):
    TEACHER = 'teacher', 'Наставник'
    LESSON = 'lesson', 'Занятие'
    STUDY = 'study', 'Учеников'


class Statistic(models.Model):
    """
    Модель статистики
    """

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистики'

    title = models.CharField(
        verbose_name="Название",
        max_length=20,
        choices=StatisticType,
        unique=True,
        error_messages={
            'unique': "Такая статистика уже есть на сайте"
        }
    )
    description = models.CharField(
        verbose_name="Описание",
        max_length=200
    )
    count = models.PositiveIntegerField(
        verbose_name="Значение статистики",
        default=10
    )
    is_display = models.BooleanField(
        verbose_name="Отображать?",
        default=True
    )
