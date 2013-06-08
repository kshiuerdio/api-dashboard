from django.conf.urls import patterns, include, url
from adashboard import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'favorites.json', views.favorites_data, name='favorites_data'),
)
