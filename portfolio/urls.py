"""
@Copyright Michelle Mark 2018
@author Michelle Mark

My portfolio urls
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.PortfolioHomeView.as_view(), name='portfolio-index'),
]
