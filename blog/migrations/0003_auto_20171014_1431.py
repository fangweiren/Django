# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171014_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_avatar',
            field=models.ImageField(upload_to='user_avatar', blank=True, default='images/01.jpg'),
        ),
    ]
