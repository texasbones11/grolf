from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^leaderboard/(?P<id>\d+)/$', views.leaderboard, name='leaderboard'),
        url(r'^scorecard/(?P<id>\d+)/$', views.scorecard, name='scorecard'),
        url(r'^useradmin$', views.useradmin, name='useradmin'),
]
