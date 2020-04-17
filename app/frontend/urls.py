from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path, re_path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='home.html'), name='url_home'),
    path(
        'private-page/',
        views.TemplateViewLoginRequired.as_view(template_name='private.html'),
        name='url_private_page',
    ),

    re_path(
        '^' + settings.PRIVATE_STATIC_URL.replace('/', '') + '/',
        views.ProtectedFileView.as_view(),
    ),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='url_login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='url_logout'
    ),
]
