# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
