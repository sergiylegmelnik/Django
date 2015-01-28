from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^hello/$', views.hello),
    url(r'^meta/$', views.display_meta),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
)
