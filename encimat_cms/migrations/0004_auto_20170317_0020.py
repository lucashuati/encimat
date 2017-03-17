# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('encimat_cms', '0003_auto_20170316_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSliderPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='encimat_cms_imagesliderpluginmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.SlugField(max_length=30)),
                ('fileUpload', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('subtitle', models.SlugField(default=b'None')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='YoutubeSliderPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='encimat_cms_youtubesliderpluginmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.SlugField(max_length=30)),
                ('url', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='imagepluginmodel',
            name='subtitle',
            field=models.SlugField(default=b'None'),
        ),
        migrations.AlterField(
            model_name='contentpluginmodel',
            name='title',
            field=models.SlugField(max_length=30),
        ),
        migrations.AlterField(
            model_name='imagepluginmodel',
            name='name',
            field=models.SlugField(max_length=30),
        ),
        migrations.AlterField(
            model_name='imagepluginmodel',
            name='title',
            field=models.SlugField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='sliderpluginmodel',
            name='name',
            field=models.SlugField(max_length=30),
        ),
        migrations.AlterField(
            model_name='sliderpluginmodel',
            name='title',
            field=models.SlugField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='textpluginmodel',
            name='name',
            field=models.SlugField(max_length=30),
        ),
        migrations.AlterField(
            model_name='textpluginmodel',
            name='title',
            field=models.SlugField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='youtubepluginmodel',
            name='name',
            field=models.SlugField(max_length=30),
        ),
        migrations.AlterField(
            model_name='youtubepluginmodel',
            name='title',
            field=models.SlugField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='youtubepluginmodel',
            name='url',
            field=models.SlugField(),
        ),
    ]
