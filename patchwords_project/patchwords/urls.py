from django.conf.urls import patterns, include, url
import views
from views import story

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^testform', views.test_form, name='testform'),
    url(r'^story/(?P<story_name_slug>[/w/-]+)/$', story, name='story'),
    url(r'^teststorylist', views.test_story_list, name='teststorylist'),
)
