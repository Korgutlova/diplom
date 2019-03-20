# Generated by Django 2.1.7 on 2019-03-13 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fls', '0009_auto_20190313_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParamResultWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(3, 'Попарные сравнения параметров'), (4, 'Ранжирование параметров')], default=3, verbose_name='Тип оценивания')),
                ('weight_value', models.FloatField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='param',
            name='result_weight',
        ),
        migrations.AddField(
            model_name='paramresultweight',
            name='param',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='param_weights', to='fls.Param'),
        ),
        migrations.AlterUniqueTogether(
            name='paramresultweight',
            unique_together={('param', 'type')},
        ),
    ]