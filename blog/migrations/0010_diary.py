# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20171118_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('body', models.TextField(verbose_name='日记')),
                ('create_time', models.DateTimeField(verbose_name='发布日期', default=django.utils.timezone.now)),
                ('author', models.ForeignKey(verbose_name='用户名', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '日记',
                'verbose_name': '日记',
                'ordering': ('-create_time',),
            },
        ),
    ]
