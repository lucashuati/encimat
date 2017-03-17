# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encimat_cms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepluginmodel',
            name='url',
        ),
        migrations.AddField(
            model_name='imagepluginmodel',
            name='fileUpload',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
