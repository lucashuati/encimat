from django.db import models
from cms.models import CMSPlugin
from django import forms

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
