# Generated by Django 2.1.7 on 2019-02-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fls', '0003_auto_20190228_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='param',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
