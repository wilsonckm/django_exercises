# Generated by Django 4.2.3 on 2023-07-11 17:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField(default=datetime.time(8, 0))),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(default='Workout.objects.first()', on_delete=django.db.models.deletion.CASCADE, to='main_app.workout'),
        ),
    ]
