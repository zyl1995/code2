from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import  settings
from registration.backends.simple.views import RegistrationView

from registration.forms import RegistrationFormNoFreeEmail






class MyRegistrationView(RegistrationView):
     def get_success_url(self, user):
         return '/rango/'

urlpatterns = patterns('',

url(r'^admin/', include(admin.site.urls)),
url(r'^rango/', include('rango.urls')),
url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
                       (r'^accounts/', include('registration.backends.simple.urls')),


)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
# Examples:

#url(r'^$', 'first_project.views.home', name='home'),
#url(r'^blog/', include('blog.urls')),

#