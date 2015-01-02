from django.conf.urls import patterns, url
from todo_list_app import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^mylist/$', views.mylist, name='mylist'),
    url(r'^tasks/$', views.tasks, name='tasks'),
)