# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('blog_id', models.CharField(max_length=100, default=0)),
                ('nickname', models.CharField(max_length=64, null=True)),
                ('mail', models.EmailField(max_length=254)),
                ('like', models.BooleanField(default=False)),
                ('content', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['blog_id'],
                'db_table': 'comment',
                'verbose_name': '评论和点赞',
            },
        ),
    ]
