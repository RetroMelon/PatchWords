from django.conf.urls import patterns, include, url
import views
from views import story

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^story/(?P<story_name_slug>[/w/-]+)/$', story, name='story'),

    #allows the homepage/categories page to request more of the most popular stories.
    url(r'^gettopstories', views.get_top_stories, name='get_top_stories'),
)
