# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0009_auto_20170317_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta',
            name='ipaddress',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='meta',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
