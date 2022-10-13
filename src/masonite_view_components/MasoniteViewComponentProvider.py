from masonite.facades import View
from masonite.providers import Provider
from . import _render, _render_with_collection


class MasoniteViewComponentProvider(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        View.add_extension('masonite_view_components.masonite_view_component_ext.MasoniteViewComponentExt')
        View.share(_render())
        View.share(_render_with_collection())

    def boot(self):
        pass
