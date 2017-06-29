from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    # url(r'^Login/(?P<username>\w{0,50})$', views.login)
    url(r'^Login/', views.login)
]