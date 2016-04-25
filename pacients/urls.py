from django.conf.urls import url
from .views import PacientList, PacientCreate, PacientUpdate

urlpatterns = [
    url(r'^$',  PacientList.as_view(),   name='show_pacients'),
    url(r'^create/$',  PacientCreate.as_view(),   name='create_pacient'),
    url(r'^update/(?P<pk>[0-9]+)/$', PacientUpdate.as_view(), name='update_pacient'),
]