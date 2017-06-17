# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 04:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20170617_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_name', to='mainapp.City')),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='dailyrate',
            name='fuel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fuel_name', to='mainapp.Fuel'),
        ),
        migrations.AlterUniqueTogether(
            name='dailyrate',
            unique_together=set([('fuel', 'city')]),
        ),
    ]
