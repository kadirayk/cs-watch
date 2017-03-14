# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0003_developer_isnobetci'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='developer',
            name='isNobetci',
            field=models.BooleanField(default=False),
        ),
    ]
