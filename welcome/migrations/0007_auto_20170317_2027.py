# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0006_auto_20170315_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(default=b'', max_length=254)),
                ('ipaddress', models.IPAddressField(default=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='developer',
            name='isNobetci',
        ),
    ]
