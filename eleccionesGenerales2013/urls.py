from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'eleccionesGenerales2013.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sobre/$','elecciones2.views.sobre'),
    url(r'^$','elecciones2.views.inicio'),
    url(r'^cantones','elecciones2.views.cantones'),

]
