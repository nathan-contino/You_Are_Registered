# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crn', models.CharField(max_length=5)),
                ('crsnum', models.CharField(max_length=10)),
                ('credits', models.CharField(max_length=5)),
                ('day', models.CharField(max_length=5)),
                ('start', models.CharField(max_length=4)),
                ('end', models.CharField(max_length=4)),
                ('building', models.CharField(max_length=8)),
                ('room', models.CharField(max_length=5)),
                ('cap', models.CharField(max_length=10)),
                ('prof', models.CharField(max_length=64)),
                ('current', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['crsnum'],
            },
        ),
    ]
