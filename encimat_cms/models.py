#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField
from django import forms
from cms.models.pagemodel import Page

class SearchPluginModel(CMSPlugin):
    links = [1,2,3,4,5,6,7,8]


    def get_links(self):
        metais = []
        pol = []
        cer = []
        avan = []
        com = []
        all = Page.objects.public().filter(template='material.html')
        for i in all:
            parent_page = Page.objects.get(id=i.parent_id)
            if parent_page.get_title() == 'Metais':
                metais.append(i)
            if parent_page.get_title() == 'Polímeros':
                pol.append(i)
            if parent_page.get_title() == 'Cerâmicos':
                cer.append(i)
            if parent_page.get_title() == 'Avançados':
                avan.append(i)
            if parent_page.get_title() == 'Compósitos':
                com.append(i)

        return {'metais':metais,'polimeros':pol,'ceramicos':cer,'avancados':avan,'compositos':com}

    @property
    def get_metais(self):
        ret =  self.get_links()
        return ret['metais']

    @property
    def get_pol(self):
        ret =  self.get_links()
        return ret['polimeros']

    @property
    def get_cer(self):
        ret =  self.get_links()
        return ret['ceramicos']

    @property
    def get_avan(self):
        ret =  self.get_links()
        return ret['avancados']

    @property
    def get_comp(self):
        ret =  self.get_links()
        return ret['compositos']

class BackGroundPluginModel(CMSPlugin):
    title = models.CharField(max_length=30)
    image = models.ImageField()


    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class SubPluginModel(CMSPlugin):
    pass

class SubCatPluginModel(CMSPlugin):
    title = models.CharField(max_length=30)

class MatPluginModel(CMSPlugin):
    pass

class PrincipaisPluginModel(CMSPlugin):
    title = models.CharField(max_length=30)
    image = models.ImageField()
    link = PageField()

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __unicode__(self):
        return self.title

class SubMatPluginModel(CMSPlugin):
    title = models.CharField(max_length=30)
    image = models.ImageField()
    link = PageField()

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __unicode__(self):
        return self.title

class EquipePluginModel(CMSPlugin):
    name = models.CharField(max_length=30)
    function = models.TextField()
    photo = models.ImageField()

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __unicode__(self):
        return self.name

class ContentPluginModel(CMSPlugin):
    title = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.title

class TextPluginModel(CMSPlugin):
    title = models.CharField(max_length = 30, blank=True, null=True)
    name = models.CharField(max_length = 30)
    text = models.TextField()
    image = models.ImageField(blank=True, null=True)

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __unicode__(self):
        return self.name

class SliderPluginModel(CMSPlugin):
    title = models.CharField(max_length = 30, blank=True, null=True)
    name = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.name

class YoutubePluginModel(CMSPlugin):
    title = models.CharField(max_length = 30, blank=True, null=True)
    name = models.CharField(max_length = 30)
    url = models.CharField(max_length = 50)


    def __unicode__(self):
        return self.name

class ImagePluginModel(CMSPlugin):
    title = models.CharField(max_length = 30, blank=True, null=True)
    name = models.CharField(max_length = 30)
    subtitle = models.CharField(default="None", max_length = 50)
    fileUpload = models.ImageField(blank=True, null=True)

    @property
    def image_url(self):
        if self.fileUpload and hasattr(self.fileUpload, 'url'):
            return self.fileUpload.url

    def __unicode__(self):
        return self.name

class ImageSliderPluginModel(CMSPlugin):
    name = models.CharField(max_length = 30)
    fileUpload = models.ImageField(blank=True, null=True)
    subtitle = models.CharField(default="None",max_length = 50)

    @property
    def image_url(self):
        if self.fileUpload and hasattr(self.fileUpload, 'url'):
            return self.fileUpload.url

    def __unicode__(self):
        return self.name

class YoutubeSliderPluginModel(CMSPlugin):
    name = models.CharField(max_length = 30)
    url = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.name
