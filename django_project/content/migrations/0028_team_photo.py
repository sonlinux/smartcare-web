# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0027_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to=b'team_pics/', null=True, verbose_name='Picture', blank=True),
        ),
    ]
