from django.conf.urls import url

from . import views

urlpatterns = [
    #ex: /fib/
    url(r'^$', views.index, name='index'),
    #ex /fib/5/
    url(r'^(?P<p>\d+)/$', views.sequence, name='sequence'),
    #ex: /fib/gen
    url(r'^gen/$', views.generate, name='generate')
]