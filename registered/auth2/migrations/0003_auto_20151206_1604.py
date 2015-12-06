# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0002_auto_20151206_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={},
        ),
        migrations.AddField(
            model_name='courses',
            name='title',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
