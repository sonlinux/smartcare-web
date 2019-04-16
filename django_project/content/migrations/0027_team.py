# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0026_hub'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=350, null=True, verbose_name='Member Name', blank=True)),
                ('title', models.CharField(max_length=350, null=True, verbose_name='Title/Position', blank=True)),
                ('content', ckeditor.fields.RichTextField(default=b'')),
                ('facebook', models.CharField(max_length=350, null=True, verbose_name='Facebook URL', blank=True)),
                ('twitter', models.CharField(max_length=350, null=True, verbose_name='Twitter URL', blank=True)),
                ('linkedin', models.CharField(max_length=350, null=True, verbose_name='Linkedin Profile', blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
