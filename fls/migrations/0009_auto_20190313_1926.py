# Generated by Django 2.1.7 on 2019-03-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fls', '0008_auto_20190313_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimationjury',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'Окончательная (абсолютная) оценка заявки'), (2, 'Попарное сравнение заявок'), (3, 'Попарные сравнения параметров'), (4, 'Ранжирование параметров')], default=1, null=True, verbose_name='Тип оценивания'),
        ),
    ]