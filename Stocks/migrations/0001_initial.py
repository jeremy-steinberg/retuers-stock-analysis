# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StockValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stock_id', models.CharField(max_length=200)),
                ('buy', models.IntegerField()),
                ('outperform', models.IntegerField()),
                ('hold', models.IntegerField()),
                ('underperform', models.IntegerField()),
                ('sell', models.IntegerField()),
                ('no_opinion', models.IntegerField()),
                ('mean', models.FloatField()),
                ('consensus', models.CharField(max_length=200)),
                ('dividend', models.CharField(max_length=200)),
                ('price_earnings', models.CharField(max_length=200)),
                ('mean_last_month', models.FloatField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
