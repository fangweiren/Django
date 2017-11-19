# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '博客', 'verbose_name_plural': '博客', 'ordering': ('-create_time',)},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': '个人资料', 'verbose_name_plural': '个人资料'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(verbose_name='用户名', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, to='blog.Category', verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(verbose_name='标签', blank=True, to='blog.Tag'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_avatar',
            field=models.ImageField(upload_to='blog/static/user_avatar', blank=True, default='images/01.jpg'),
        ),
    ]
