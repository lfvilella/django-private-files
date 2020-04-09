import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from django.views.generic import TemplateView
from django.views.static import serve


class HomePageView(TemplateView):
    template_name = 'home.html'


class PrivatePageView(LoginRequiredMixin, TemplateView):
    template_name = 'private.html'


class ProtectedFileView(View):

    def _extract_file_path_from_url(self, request):
        return request.path.replace(settings.PRIVATE_STATIC_URL, '')

    def _serve_staticfile_by_django(self, request):
        url_file_path = self._extract_file_path_from_url(request)
        for _dir in settings.STATICFILES_DIRS:
            filepath = os.path.join(_dir, settings.PRIVATE_STATICFILES_FOLDER, url_file_path)
            if not os.path.isfile(filepath):
                continue
            return serve(request, os.path.basename(filepath), os.path.dirname(filepath))

    def _serve_staticfile_by_nginx(self, request):
        url_file_path = self._extract_file_path_from_url(request)
        response = HttpResponse()
        response['X-Accel-Redirect'] = '/internal/protected/' + url_file_path
        response['X-Accel-Buffering'] = 'no'
        return response

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404()

        if settings.STATICFILES_SERVING_BY_NGINX:
            return self._serve_staticfile_by_nginx(request)

        if settings.STATICFILES_SERVING_BY_DJANGO:
            return self._serve_staticfile_by_django(request)

        raise Http404()
