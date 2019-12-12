from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'main/portfolio.html'
    http_method_names = ['get']
