from django.conf import settings
from django.urls import path, re_path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.HomePageView.as_view()),
    path('private-page', views.PrivatePageView.as_view()),

    re_path(
        '^' + settings.PRIVATE_STATIC_URL.replace('/', '') + '/',
        views.ProtectedFileView.as_view(),
    ),
]
