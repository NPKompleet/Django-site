# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
