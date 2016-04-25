from django.conf.urls import include, url
from .view import login, create

url_patterns = [
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', create, name='create'),
]