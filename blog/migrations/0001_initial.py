# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='发布日期')),
                ('update_time', models.DateTimeField(verbose_name='最后修改日期', auto_now=True)),
            ],
            options={
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(verbose_name='用户名', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(verbose_name='密  码', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(to='blog.User'),
        ),
    ]
