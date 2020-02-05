from django.views.generic import TemplateView
from django.conf import settings
from sheep_service.api import SheepApi


# Create your views here.

class MapView(TemplateView):
    template_name = 'map/map.html'
    api = SheepApi()

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)

        sheep = self.api.get_sheep_str()
        context['sheep'] = sheep

        context['DEBUG'] = settings.DEBUG

        return context
