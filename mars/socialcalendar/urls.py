from django.conf.urls import patterns, include, url
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns =patterns('',

    url(r'^caldata/$', views.CaldataView.as_view()),
)