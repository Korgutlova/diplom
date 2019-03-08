# Generated by Django 2.1.7 on 2019-03-08 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0003_weights_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupWeights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30, unique=True)),
                ('weights', models.TextField()),
                ('type', models.CharField(choices=[('kfavg', 'KF+AVG'), ('kf', 'KF'), ('avg', 'AVG'), ('c', 'COUNT')], max_length=10)),
            ],
        ),
    ]
