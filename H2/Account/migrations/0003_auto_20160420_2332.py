# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20160420_2322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户资料'},
        ),
        migrations.AlterModelTable(
            name='userprofile',
            table='account_user_profile',
        ),
    ]
