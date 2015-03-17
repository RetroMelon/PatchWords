from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^story/(?P<story_name_slug>[/w/-]+)/$', story, name='story'),
    url(r'^category/(?P<category_name_slug>[/w/-]+)/$', category, name='category'),
    url(r'^search/q', search, name='search'),
    #allows the homepage/categories page to request more of the most popular stories.
    url(r'^gettopstories', get_top_stories, name='get_top_stories'),
)
