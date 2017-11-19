# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171014_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_avatar',
            field=models.ImageField(blank=True, verbose_name='头像', upload_to='avatar', default='images/01.jpg'),
        ),
    ]
