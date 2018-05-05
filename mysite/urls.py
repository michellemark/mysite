"""
@Copyright Michelle Mark 2018
@author Michelle Mark

All paths start here...
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('my-admin/', admin.site.urls),
    # path('portfolio', include('portfolio.urls')),
    path('', include('main_pages.urls')),
]
