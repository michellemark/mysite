"""
@Copyright Michelle Mark 2018
@author Michelle Mark

Views for the main pages of the site
"""
from itertools import permutations

from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import ContactMeForm, PermuteForm


class ContactMeView(TemplateView):
    template_name = 'contact-me-form.html'
    form_class = ContactMeForm
    success_url = 'contact-form-thanks'

    def get_context_data(self, **kwargs):
        context = super(ContactMeView, self).get_context_data(**kwargs)
        context['page_title'] = "Contact Me"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class(request.POST)

        if context['form'].is_valid():
            context['form'].save()

            return redirect(self.success_url)

        return render(request, self.template_name, context)


class ContactMeThanksView(TemplateView):
    template_name = 'contact-me-thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ContactMeThanksView, self).get_context_data(**kwargs)
        context['page_title'] = "Thank You"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['page_title'] = "Home"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context


class PermuteView(TemplateView):
    template_name = 'permute.html'
    form_class = PermuteForm

    def get_context_data(self, **kwargs):
        context = super(PermuteView, self).get_context_data(**kwargs)
        context['page_title'] = "Permute a Value Exercise"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = self.form_class(request.POST)

        if context['form'].is_valid():
            context['value_mutated'] = context['form'].cleaned_data.get('permute_value')
            all_mutations = list(permutations(context['value_mutated']))

            if all_mutations and len(all_mutations) > 0:
                context['all_permutations'] = []

                for mutation in all_mutations:
                    context['all_permutations'].append("".join(mutation))

        return render(request, self.template_name, context)


class ResumeView(TemplateView):
    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['page_title'] = "My Resume"
        context['extra_css'] = []
        context['extra_javascript'] = []

        return context
