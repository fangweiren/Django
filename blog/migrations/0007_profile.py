# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20171021_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('user_avatar', models.ImageField(default='images/01.jpg', blank=True, upload_to='avatar', verbose_name='头像')),
                ('sex', models.CharField(max_length=1, choices=[('M', '男'), ('F', '女')], verbose_name='性别')),
                ('birthday', models.DateTimeField(blank=True, verbose_name='出生年月')),
                ('register_DateTime', models.DateTimeField(blank=True, verbose_name='注册日期')),
                ('login_DateTime', models.DateTimeField(blank=True, verbose_name='最后登录日期')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name_plural': '个人资料',
                'verbose_name': '个人资料',
            },
        ),
    ]
