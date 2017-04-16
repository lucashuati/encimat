# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('encimat_cms', '0003_searchpluginmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrincipaisPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='encimat_cms_principaispluginmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to=b'')),
                ('link', cms.models.fields.PageField(to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
