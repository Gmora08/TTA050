from django.conf.urls import url
from .views import create, log_in, log_out

urlpatterns = [
    url(r'^login/$',  log_in,   name='login'),
    url(r'^singup/$', create,  name='singup'),
    url(r'^logout/$', log_out, name='logout'),
]