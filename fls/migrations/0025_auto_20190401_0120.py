# Generated by Django 2.1.7 on 2019-03-31 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fls', '0024_auto_20190327_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='subparam',
            name='max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='param',
            name='max',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]