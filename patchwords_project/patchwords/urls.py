from django.conf.urls import patterns, include, url
import views
from views import story

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^testform', views.test_form, name='testform'),
<<<<<<< HEAD
    url(r'^story/(?P<story_name_slug>[/w/-]+)/$', story, name='story'),
=======
    url(r'^teststorieschunk', views.test_stories_chunk, name='teststorieschunk'),
>>>>>>> 5f450ae1247ff8a8ecb7dc2ca28c0218ab252368
)
