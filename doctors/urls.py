from django.conf.urls import url
from .views import create, login

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^singup/$', create, name='singup'),
]