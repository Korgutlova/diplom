# Generated by Django 2.1.7 on 2019-03-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0005_groupweights_deviations_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupweights',
            name='group_name',
            field=models.CharField(max_length=30),
        ),
    ]
