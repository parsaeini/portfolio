import os

from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'main/portfolio.html'
    http_method_names = ['get']


#
def download_resume(request):
    file_name = 'parsa-eini-resume.pdf'
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            response = HttpResponse(
                file.read(),
                content_type="application/force-download"
            )
            content_disposition = 'inline; filename=' + os.path.basename(file_path)

            response['Content-Disposition'] = content_disposition
            return response
    raise Http404
