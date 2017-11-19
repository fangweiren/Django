# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20171118_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_avatar',
            field=models.ImageField(upload_to='avatar', verbose_name='头像', default='BX3.jpg'),
        ),
    ]
