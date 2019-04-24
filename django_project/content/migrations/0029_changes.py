# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0028_team_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Changes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Title', blank=True)),
                ('content', ckeditor.fields.RichTextField(null=True, verbose_name='Release Notes', blank=True)),
                ('published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
