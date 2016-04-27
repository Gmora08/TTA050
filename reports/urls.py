from django.conf.urls import url
from .views import ReportCreate

urlpatterns = [
    url(r'^new/(?P<pk>\d+)/$',  ReportCreate.as_view(),   name='new_report'),
]