# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='分类', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=100)),
                ('body', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(verbose_name='发布日期', default=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(verbose_name='最后修改日期', auto_now=True)),
                ('read_amount', models.IntegerField(verbose_name='浏览', default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='blog.Category', blank=True)),
            ],
            options={
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('user_avatar', models.ImageField(upload_to='user_avatar', default='images/01.jpg', blank=True)),
                ('sex', models.CharField(verbose_name='性别', max_length=1, choices=[('M', '男'), ('F', '女')])),
                ('birthday', models.DateTimeField(verbose_name='出生年月', blank=True)),
                ('register_DateTime', models.DateTimeField(verbose_name='注册日期', blank=True)),
                ('login_DateTime', models.DateTimeField(verbose_name='最后登录日期', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='标签', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', blank=True),
        ),
    ]
