from django.conf.urls import url
from .views import PacientList, PacientCreate, PacientUpdate, PacientDelete, PacientDetail

urlpatterns = [
    url(r'^$',  PacientList.as_view(),   name='index_pacients'),
    url(r'^new/$',  PacientCreate.as_view(),   name='create_pacient'),
    url(r'^(?P<pk>[0-9]+)/update/$', PacientUpdate.as_view(), name='update_pacient'),
    url(r'^(?P<pk>[0-9]+)/delete/$', PacientDelete.as_view(), name='delete_pacient'),
    url(r'^(?P<pk>[0-9]+)/$', PacientDetail.as_view(), name='show_pacient')
]