from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^leaderboard/(?P<id>\d+)/$', views.leaderboard, name='leaderboard'),
        url(r'^scorecard/(?P<id>\d+)/$', views.scorecard, name='scorecard'),
        url(r'^useradmin$', views.useradmin, name='useradmin'),
        url(r'^scorecard2/(?P<id>\d+)/$', views.scorecard, name='scorecard2'),
        url(r'^scorecard3/(?P<id>\d+)/$', views.scorecard, name='scorecard3'),
        url(r'^scorecard4/(?P<id>\d+)/$', views.scorecard, name='scorecard4'),
        url(r'^scorecard5/(?P<id>\d+)/$', views.scorecard, name='scorecard5'),
        url(r'^scorecard6/(?P<id>\d+)/$', views.scorecard, name='scorecard6'),
        url(r'^scorecard7/(?P<id>\d+)/$', views.scorecard, name='scorecard7'),
        url(r'^scorecard8/(?P<id>\d+)/$', views.scorecard, name='scorecard8'),
        url(r'^scorecard9/(?P<id>\d+)/$', views.scorecard, name='scorecard9'),
        url(r'^scorecard10/(?P<id>\d+)/$', views.scorecard, name='scorecard10'),
        url(r'^scorecard11/(?P<id>\d+)/$', views.scorecard, name='scorecard11'),
        url(r'^scorecard12/(?P<id>\d+)/$', views.scorecard, name='scorecard12'),
        url(r'^scorecard13/(?P<id>\d+)/$', views.scorecard, name='scorecard13'),
        url(r'^scorecard14/(?P<id>\d+)/$', views.scorecard, name='scorecard14'),
        url(r'^scorecard15/(?P<id>\d+)/$', views.scorecard, name='scorecard15'),
        url(r'^scorecard16/(?P<id>\d+)/$', views.scorecard, name='scorecard16'),
        url(r'^scorecard17/(?P<id>\d+)/$', views.scorecard, name='scorecard17'),
        url(r'^scorecard18/(?P<id>\d+)/$', views.scorecard, name='scorecard18'),
        url(r'^login/(?P<id>\d+)/$', views.login, name='login'),
]
