from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raverflavour.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^payment/', include('store.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'splash.views.home', name='home'),
)
