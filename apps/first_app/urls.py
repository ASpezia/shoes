from django.conf.urls import url
from . import views           # This line is new!



urlpatterns = [
    url(r'^$', views.index),
    url(r'^shoes$', views.shoes),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^sell$',views.sell),
    url(r'^remove$', views.remove),
    url(r'^logout$', views.logout),
    url(r'^logoutfunc$', views.logoutfunc),
     # This line has changed!
  ]
