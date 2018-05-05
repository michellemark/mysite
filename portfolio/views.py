"""
@Copyright Michelle Mark 2018
@author Michelle Mark

My portfolio views
"""
from django.views.generic import TemplateView


class PortfolioHomeView(TemplateView):
    template_name = 'portfolio-home.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioHomeView, self).get_context_data(**kwargs)
        context['page_title'] = "My Portfolio Home"
        context['extra_css'] = ['css/album.css']
        context['extra_javascript'] = []

