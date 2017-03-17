# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0007_auto_20170317_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='name',
            field=models.CharField(default=b'', max_length=64),
        ),
        migrations.AlterField(
            model_name='meta',
            name='ipaddress',
            field=models.GenericIPAddressField(default=b''),
        ),
    ]
