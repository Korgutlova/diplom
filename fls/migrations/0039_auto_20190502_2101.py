# Generated by Django 2.1.7 on 2019-05-02 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fls', '0038_merge_20190502_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightParamJury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_value', models.FloatField(default=0)),
                ('jury', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jury_param_weights', to='fls.CustomUser', verbose_name='Жюри')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='weightcriterionjury',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='weightcriterionjury',
            name='criterion',
        ),
        migrations.RemoveField(
            model_name='weightcriterionjury',
            name='jury',
        ),
        migrations.AlterField(
            model_name='competition',
            name='method_of_estimate',
            field=models.IntegerField(blank=True, choices=[(1, 'Ручная оценка'), (2, 'Взвешенное суммирование'), (3, 'Расчёт по формуле')], default=1, null=True, verbose_name='Метод оценивания'),
        ),
        migrations.AlterField(
            model_name='criterionweight',
            name='criterion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criterion_weights', to='fls.Criterion', unique=True),
        ),
        migrations.AlterField(
            model_name='estimationjury',
            name='type',
            field=models.IntegerField(blank=True, choices=[(1, 'Ручная оценка'), (2, 'Взвешенное суммирование')], default=1, null=True, verbose_name='Тип оценивания'),
        ),
        migrations.AlterField(
            model_name='requestestimation',
            name='type',
            field=models.IntegerField(choices=[(1, 'Ручная оценка'), (2, 'Взвешенное суммирование'), (3, 'Расчёт по формуле')], default=1, verbose_name='Тип оценивания'),
        ),
        migrations.AlterUniqueTogether(
            name='criterion',
            unique_together={('competition', 'name')},
        ),
        migrations.AlterUniqueTogether(
            name='criterionweight',
            unique_together=set(),
        ),
        migrations.DeleteModel(
            name='WeightCriterionJury',
        ),
        migrations.AddField(
            model_name='weightparamjury',
            name='param',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='param_weights', to='fls.Criterion'),
        ),
        migrations.RemoveField(
            model_name='criterionweight',
            name='type',
        ),
        migrations.AlterUniqueTogether(
            name='weightparamjury',
            unique_together={('jury', 'param')},
        ),
    ]