from django.conf.urls import  url
import booktest.views

urlpatterns = [
    url(r'^$',booktest.views.index),
    url(r'^area/$',booktest.views.area),
    url(r'^area/pro/$',booktest.views.pro),
    url(r'^area/city(\d+)/$',booktest.views.city),
]