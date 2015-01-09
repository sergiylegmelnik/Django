from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import hello, home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),

)
