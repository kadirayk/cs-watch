# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0002_developer'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='isNobetci',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
