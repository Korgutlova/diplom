# Generated by Django 2.1.7 on 2019-03-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0002_auto_20190222_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='weights',
            name='type',
            field=models.CharField(choices=[('kfavg', 'KF+AVG'), ('kf', 'KF'), ('avg', 'AVG'), ('c', 'COUNT')], default='kfavg', max_length=10),
        ),
    ]
