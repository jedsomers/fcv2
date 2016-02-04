from django.conf.urls import patterns, url
from fc_core import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'))