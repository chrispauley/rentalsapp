# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentalsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('erc_firstName', models.CharField(max_length=200)),
                ('erc_initial', models.CharField(max_length=1)),
                ('erc_lastName', models.CharField(max_length=200)),
                ('erc_cellPhone', models.CharField(max_length=10)),
                ('erc_street', models.CharField(max_length=200)),
                ('erc_city', models.CharField(max_length=200)),
                ('erc_state', models.CharField(max_length=2)),
                ('erc_zip', models.CharField(max_length=5)),
                ('erc_weight', models.CharField(max_length=10)),
                ('erc_height', models.CharField(max_length=10)),
                ('erc_age', models.IntegerField()),
                ('erc_emailAddress', models.CharField(max_length=200)),
                ('erc_skierType', models.CharField(max_length=10)),
                ('erc_snowboardStance', models.CharField(max_length=10)),
            ],
        ),
    ]
