from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^home/$', views.home, name='home'),
    re_path(r'^(?P<room_name>.*)/$', views.room, name='room'),
]