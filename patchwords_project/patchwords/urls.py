from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', home, name='home'),
    url(r'^story/(?P<story_name_slug>[\w-]+)/$', story, name='story'),
    url(r'^category/(?P<category_name_slug>[\w-]+)/$', category, name='category'),
    url(r'^profile/(?P<username>\w{0,50})/$',profile,name='profile'),
    url(r'^edit_profile/$',edit_profile,name='edit_profile'),
    url(r'^allcategories', all_categories, name='all_categories'),
    url(r'^search/(?P<q>\w+)', search, name='search'),
    #allows the homepage/categories page to request more of the most popular stories.
    url(r'^gettopstories', get_top_stories, name='get_top_stories'),
    url(r'getsubtree/(?P<paragraph_id>\d+)/$', render_most_popular_subtree ,name='getsubtree'),
)
