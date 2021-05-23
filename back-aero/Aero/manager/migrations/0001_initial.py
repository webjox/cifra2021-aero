# Generated by Django 3.2.3 on 2021-05-23 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('long', models.FloatField(verbose_name='Долгота')),
                ('issue', models.CharField(max_length=255, verbose_name='Задача')),
                ('unit', models.CharField(max_length=100, verbose_name='Юнит')),
                ('time_created', models.DateTimeField(auto_now=True, verbose_name='Время создания задачи')),
                ('time_lead', models.IntegerField(verbose_name='Время выполнения задачи')),
                ('time_finish', models.DateTimeField(auto_now=True, verbose_name='Время закрытия задачи')),
                ('person', models.CharField(max_length=100, verbose_name='Персонаж')),
                ('status', models.CharField(choices=[('New', 'Новая'), ('Assigned', 'Назначена'), ('Accepted', 'Принял задачу'), ('In_progress', 'В работе'), ('Check', 'Проверка'), ('Completed', 'Завершена')], default='Новая', max_length=100, verbose_name='Статус исполнения задачи')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_telegram', models.IntegerField(verbose_name='ID телеграмма работника')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('post', models.CharField(max_length=100, verbose_name='Занимаемая должность')),
            ],
            options={
                'verbose_name': 'Персонаж',
                'verbose_name_plural': 'Персонажи',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название должности')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Проблема')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Проблема',
                'verbose_name_plural': 'Проблемы',
            },
        ),
        migrations.CreateModel(
            name='Shifts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название смены')),
                ('shift_duration', models.TimeField(verbose_name='Длительность смены')),
            ],
            options={
                'verbose_name': 'Смена',
                'verbose_name_plural': 'Смены',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название техники')),
                ('free', models.BooleanField(default=True, verbose_name='Статус доступности')),
            ],
            options={
                'verbose_name': 'Юнит',
                'verbose_name_plural': 'Юниты',
            },
        ),
    ]
