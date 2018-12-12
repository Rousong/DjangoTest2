from django.conf.urls import  url
import booktest.views

urlpatterns = [
    url(r'^$',booktest.views.index),
    url(r'^area/$',booktest.views.area),
    url(r'^area/(\d+)/$',booktest.views.area2),
]