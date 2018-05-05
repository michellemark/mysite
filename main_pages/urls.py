"""
@Copyright Michelle Mark 2018
@author Michelle Mark

"""
from django.urls import path

from . import views


urlpatterns = [
    path('contact/', views.ContactMeView.as_view(), name='contact-form'),
    path('thanks/', views.ContactMeThanksView.as_view(), name='contact-form-thanks'),
    # path('resume', views.ResumeView.as_view(), name='resume'),
    path('', views.HomeView.as_view(), name='home'),
]
