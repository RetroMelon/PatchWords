from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^testform', views.test_form, name='testform'),
    url(r'^teststorieschunk', views.test_stories_chunk, name='teststorieschunk'),
)
