# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='building',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='cap',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='credits',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='crn',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='crsnum',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='current',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='day',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='end',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='room',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='courses',
            name='start',
            field=models.CharField(max_length=64),
        ),
    ]
