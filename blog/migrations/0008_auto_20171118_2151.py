# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_avatar',
            field=models.ImageField(verbose_name='头像', default='images/01.jpg', upload_to='avatar'),
        ),
    ]
