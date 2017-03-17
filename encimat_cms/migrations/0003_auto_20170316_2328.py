# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encimat_cms', '0002_auto_20170315_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepluginmodel',
            name='title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='sliderpluginmodel',
            name='title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='textpluginmodel',
            name='title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='youtubepluginmodel',
            name='title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='youtubepluginmodel',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
