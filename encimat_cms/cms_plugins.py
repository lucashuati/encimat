from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from encimat_cms.models import *
from django.utils.translation import ugettext as _


class ContentPluginPublisher(CMSPluginBase):
    model = ContentPluginModel  # model where plugin data are saved
    module = _("Encimat")
    name = _("Conteudo")  # name of the plugin in the interface
    render_template = "polls_cms_integration/content.html"
    allow_children = True
    child_classes = ['TextPluginPublisher', 'SliderPluginPublisher', 'ImagePluginPublisher', 'YoutubePluginPublisher']

    def render(self, context, instance, placeholder):
        context = super(ContentPluginPublisher, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(ContentPluginPublisher)  # register the plugin

class SliderPluginPublisher(CMSPluginBase):
    model = SliderPluginModel  # model where plugin data are saved
    module = _("Encimat")
    name = _("Slider")  # name of the plugin in the interface
    render_template = "polls_cms_integration/slider.html"
    require_parent = True
    allow_children = True
    child_classes = ['ImageSliderPluginPublisher', 'YoutubeSliderPluginPublisher']

    def render(self, context, instance, placeholder):
        context = super(SliderPluginPublisher, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(SliderPluginPublisher)  # register the plugin

class TextPluginPublisher(CMSPluginBase):
    model = TextPluginModel  # model where plugin data are saved
    module = _("Encimat")
    name = _("Texto")  # name of the plugin in the interface
    render_template = "polls_cms_integration/text.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super(TextPluginPublisher, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(TextPluginPublisher)  # register the plugin

class YoutubePluginPublisher(CMSPluginBase):
    model = YoutubePluginModel  # model where plugin data are saved
    module = _("Encimat")
    name = _("Video do Youtube")  # name of the plugin in the interface
    render_template = "polls_cms_integration/youtube.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super(YoutubePluginPublisher, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(YoutubePluginPublisher)  # register the plugin

class ImagePluginPublisher(CMSPluginBase):
    model = ImagePluginModel  # model where plugin data are saved
    module = _("Encimat")
    name = _("Imagem")  # name of the plugin in the interface
    render_template = "polls_cms_integration/image.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super(ImagePluginPublisher, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(ImagePluginPublisher)  # register the plugin

class ImageSliderPluginPublisher(CMSPluginBase):
    model = ImageSliderPluginModel  # model where plugin data are saved
    module = _("Encimat")
    name = _("Imagem")  # name of the plugin in the interface
    render_template = "polls_cms_integration/imageSlider.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super(ImageSliderPluginPublisher, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(ImageSliderPluginPublisher)  # register the plugin

class YoutubeSliderPluginPublisher(CMSPluginBase):
    model = YoutubeSliderPluginModel  # model where plugin data are saved
    module = _("Encimat")
    name = _("Video do Youtube")  # name of the plugin in the interface
    render_template = "polls_cms_integration/youtubeSlider.html"
    require_parent = True

    def render(self, context, instance, placeholder):
        context = super(YoutubeSliderPluginPublisher, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(YoutubeSliderPluginPublisher)  # register the plugin
