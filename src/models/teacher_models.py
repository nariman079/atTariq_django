from django.db import models
from enum import Enum


class Gender(models.TextChoices):
    MALE = "male", 'Мужской'
    FEMALE = "female", "Женский"


class Discipline(models.Model):
    """
    Модель дисциплины
    """

    class Meta:
        verbose_name = "Дисциплина"
        verbose_name_plural = "Дисциплины"

    title = models.CharField(
        verbose_name="Название",
        max_length=255,
        help_text="Название дисциплины"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Описание дисциплины"
    )
    priority = models.IntegerField(
        verbose_name="Приоритет",
        default=0,
        help_text="Приоритет дисциплины"
    )

    def __str__(self):
        return self.title


class Teacher(models.Model):
    """
    Модель учителя
    """

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    telegram_id = models.CharField(
        verbose_name="Telegram ID",
        max_length=255,
        unique=True,
        help_text="ID учителя в Telegram"
    )
    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        help_text="Email учителя"
    )
    name = models.CharField(
        verbose_name="Имя",
        max_length=255,
        help_text="Имя учителя"
    )
    surname = models.CharField(
        verbose_name="Фамилия",
        max_length=255,
        help_text="Фамилия учителя"
    )
    experience = models.IntegerField(
        verbose_name="Опыт",
        help_text="Опыт учителя в годах"
    )
    about = models.TextField(
        verbose_name="О себе",
        help_text="Информация об учителе"
    )
    opportunities = models.TextField(
        verbose_name="Возможности",
        help_text="Возможности учителя"
    )
    study_methods = models.TextField(
        verbose_name="Методы обучения",
        help_text="Методы обучения учителя"
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=0,
        default=0,
        help_text="Стоимость услуг учителя"
    )
    gender = models.CharField(
        verbose_name="Пол",
        max_length=20,
        default=Gender.MALE,
        help_text="Пол учителя"
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to='teachers/images/',
        null=True,
        blank=True,
        help_text="Изображение учителя"
    )
    successful_lesson_count = models.PositiveIntegerField(
        verbose_name="Количество успешно проведенных уроков",
        default=0
    )
    disciplines = models.ManyToManyField(
        Discipline,
        verbose_name="Дисциплины",
        related_name='teachers',
        help_text="Дисциплины, преподаваемые учителем"
    )

    def __str__(self):
        return f"{self.name} {self.surname}"


class Customer(models.Model):
    """
    Модель клиенты
    """

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    name = models.CharField(
        verbose_name="Имя",
        max_length=255,
        help_text="Имя клиента"
    )
    surname = models.CharField(
        verbose_name="Фамилия"
    )
    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        help_text="Email клиента"
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Модель отзыв учителю
    """

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Учитель",
        help_text="Учитель, которому оставлен отзыв"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Клиент",
        help_text="Клиент, оставивший отзыв"
    )
    rating = models.IntegerField(
        verbose_name="Рейтинг",
        help_text="Рейтинг учителя"
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        help_text="Комментарий клиента"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата создания отзыва"
    )

    def __str__(self):
        return f"Отзыв от {self.customer.name} для {self.teacher.name}"
