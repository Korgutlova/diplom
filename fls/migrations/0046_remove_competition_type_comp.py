# Generated by Django 2.1.7 on 2019-05-04 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fls', '0045_auto_20190504_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='type_comp',
        ),
    ]