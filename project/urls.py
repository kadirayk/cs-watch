from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health, addDeveloper, deleteDeveloper, nobetcify

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^deleteDeveloper$', deleteDeveloper),
    url(r'^addDeveloper$', addDeveloper),
    url(r'^nobetcify$', nobetcify),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
]
