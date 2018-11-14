from django.conf.urls import  url
import booktest.views

urlpatterns = [
    url(r'^$',booktest.views.index),
]