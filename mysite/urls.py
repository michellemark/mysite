"""
@Copyright Michelle Mark 2018
@author Michelle Mark

All paths start here...
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}


urlpatterns = [
    path('my-admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('portfolio', include('portfolio.urls')),
    path('', include('main_pages.urls')),
]
