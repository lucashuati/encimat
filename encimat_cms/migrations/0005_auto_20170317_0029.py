# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encimat_cms', '0004_auto_20170317_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpluginmodel',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='imagepluginmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='imagepluginmodel',
            name='subtitle',
            field=models.CharField(default=b'None', max_length=50),
        ),
        migrations.AlterField(
            model_name='imagepluginmodel',
            name='title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='imagesliderpluginmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='imagesliderpluginmodel',
            name='subtitle',
            field=models.CharField(default=b'None', max_length=50),
        ),
        migrations.AlterField(
            model_name='sliderpluginmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='sliderpluginmodel',
            name='title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='textpluginmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='textpluginmodel',
            name='title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='youtubepluginmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='youtubepluginmodel',
            name='title',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='youtubepluginmodel',
            name='url',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='youtubesliderpluginmodel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='youtubesliderpluginmodel',
            name='url',
            field=models.CharField(max_length=50),
        ),
    ]
