from settings import *
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
import registration.backends.default.urls
from registration.backends.simple.views import RegistrationView
from patchwords.forms import Registration
from patchwords.views import profile

class MyRegistrationView(RegistrationView):
     def get_form_class(self,request):
         return Registration
     def get_success_url(self,request,user):
         return '/patchwords/'


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^patchwords/', include('patchwords.urls')),
    url(r'^register/',MyRegistrationView.as_view(form_class=Registration),name='registration_register'),
    url(r'^', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
