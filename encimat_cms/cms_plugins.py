from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from encimat_cms.models import *
from django.utils.translation import ugettext as _

class PrincipaisPlugin(CMSPluginBase):
    model = PrincipaisPluginModel
    module = ("Encimat")
    name = _("Principais")
    render_template = "polls_cms_integration/principais.html"

    def render(self, context, instance, placeholder):
        context = super(PrincipaisPlugin, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(PrincipaisPlugin)

class SearchPlugin(CMSPluginBase):
    model = SearchPluginModel
    module = ("Search")
    name = _("Busca")
    render_template = "polls_cms_integration/search.html"

    def render(self, context, instance, placeholder):
        context = super(SearchPlugin, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(SearchPlugin)

class BackGroundPlugin(CMSPluginBase):
    model = BackGroundPluginModel
    module = ("ENCIMAT")
    name = _("Imagem de Fundo")
    render_template = "polls_cms_integration/bg.html"

    def render(self, context, instance, placeholder):
        context = super(BackGroundPlugin, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(BackGroundPlugin)

class SubPlugin(CMSPluginBase):
    model = SubPluginModel
    module = ("ENCIMAT")
    name = _("Container Categoria")
    render_template = "polls_cms_integration/sub.html"
    allow_children = True
    child_classes = ['SubCatPlugin']

    def render(self, context, instance, placeholder):
        context = super(SubPlugin, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(SubPlugin)

class SubCatPlugin(CMSPluginBase):
    model = SubCatPluginModel
    module = ("ENCIMAT")
    name = _("Sub Categoria")
    render_template = "polls_cms_integration/subcat.html"
    allow_children = True
    child_classes = ['SubPlugin', 'MatPlugin']

    def render(self, context, instance, placeholder):
        context = super(SubCatPlugin, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(SubCatPlugin)

class MatPlugin(CMSPluginBase):
    model = MatPluginModel
    module = ("ENCIMAT")
    name = _("Container Material")
    render_template = "polls_cms_integration/mat.html"
    allow_children = True
    child_classes = ['SubMatPlugin']

    def render(self, context, instance, placeholder):
        context = super(MatPlugin, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(MatPlugin)

class SubMatPlugin(CMSPluginBase):
    model = SubMatPluginModel
    module = ("ENCIMAT")
    name = _("Container SubMaterial")
    render_template = "polls_cms_integration/submat.html"

    def render(self, context, instance, placeholder):
        context = super(SubMatPlugin, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(SubMatPlugin)

class EquipePlugin(CMSPluginBase):
    model = EquipePluginModel  # model where plugin data are saved
    module = _("Encimat")
    name = _("Equipe")  # name of the plugin in the interface
    render_template = "polls_cms_integration/equipe.html"

    def render(self, context, instance, placeholder):
        context = super(EquipePlugin, self).render(context,instance,placeholder)
        return context

plugin_pool.register_plugin(EquipePlugin)  # register the plugin

class ContentPluginPublisher(CMSPluginBase):
    model = ContentPluginModel  # model where plugin data are saved
    module = _("Encimat")
    name = _("Conteudo")  # name of the plugin in the interface
    render_template = "polls_cms_integration/content.html"
    allow_children = True
    child_classes = ['TextPlugin', 'SliderPluginPublisher', 'ImagePluginPublisher', 'YoutubePluginPublisher']

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
