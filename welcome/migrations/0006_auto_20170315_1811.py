# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0005_audit'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='lastvisit',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='audit',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
