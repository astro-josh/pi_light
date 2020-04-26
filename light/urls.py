from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^submit_command/$', views.submit_command, name="submit_command"),
    path('command/', views.LightCommandViewAjax.as_view(), name='Command'),
]
