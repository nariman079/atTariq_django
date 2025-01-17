# Generated by Django 5.0.7 on 2024-07-30 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя клиента', max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('email', models.EmailField(help_text='Email клиента', max_length=254, unique=True, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название дисциплины', max_length=255, verbose_name='Название')),
                ('description', models.TextField(help_text='Описание дисциплины', verbose_name='Описание')),
                ('priority', models.IntegerField(default=0, help_text='Приоритет дисциплины', verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(help_text='ID учителя в Telegram', max_length=255, unique=True, verbose_name='Telegram ID')),
                ('email', models.EmailField(help_text='Email учителя', max_length=254, unique=True, verbose_name='Email')),
                ('name', models.CharField(help_text='Имя учителя', max_length=255, verbose_name='Имя')),
                ('surname', models.CharField(help_text='Фамилия учителя', max_length=255, verbose_name='Фамилия')),
                ('experience', models.IntegerField(help_text='Опыт учителя в годах', verbose_name='Опыт')),
                ('about', models.TextField(help_text='Информация об учителе', verbose_name='О себе')),
                ('opportunities', models.TextField(help_text='Возможности учителя', verbose_name='Возможности')),
                ('study_methods', models.TextField(help_text='Методы обучения учителя', verbose_name='Методы обучения')),
                ('price', models.DecimalField(decimal_places=0, default=0, help_text='Стоимость услуг учителя', max_digits=10, verbose_name='Цена')),
                ('gender', models.CharField(default='male', help_text='Пол учителя', max_length=20, verbose_name='Пол')),
                ('image', models.ImageField(blank=True, help_text='Изображение учителя', null=True, upload_to='teachers/images/', verbose_name='Изображение')),
                ('successful_lesson_count', models.PositiveIntegerField(default=0, verbose_name='Количество успешно проведенных уроков')),
                ('disciplines', models.ManyToManyField(help_text='Дисциплины, преподаваемые учителем', related_name='teachers', to='src.discipline', verbose_name='Дисциплины')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(help_text='Рейтинг учителя', verbose_name='Рейтинг')),
                ('comment', models.TextField(help_text='Комментарий клиента', verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата создания отзыва', verbose_name='Дата создания')),
                ('customer', models.ForeignKey(help_text='Клиент, оставивший отзыв', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='src.customer', verbose_name='Клиент')),
                ('teacher', models.ForeignKey(help_text='Учитель, которому оставлен отзыв', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='src.teacher', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
