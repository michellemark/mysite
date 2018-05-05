"""
@Copyright Michelle Mark 2018
@author Michelle Mark

Views for the main pages of the site
"""
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.core.mail import send_mail

from .forms import ContactMeForm


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
            my_email = getattr(settings, "DEFAULT_FROM_EMAIL")
            send_mail(
                "New Contact Me Submission",
                "A new contact me submission!<br><br><a href='https://michellemark.me/my-admin/'>Visit the admin</a>",
                my_email,
                [my_email],
                fail_silently=False,
            )

            return redirect(self.success_url)

        return render(request, self.template_name, context)


class ContactMeThanksView(TemplateView):
    template_name = 'contact-me-thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ContactMeThanksView, self).get_context_data(**kwargs)
        context['page_title'] = "Thank You"
        context['extra_css'] = []
        context['extra_javascript'] = []


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['page_title'] = "Home"
        context['extra_css'] = []
        context['extra_javascript'] = []


class ResumeView(TemplateView):
    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['page_title'] = "My Resume"
        context['extra_css'] = []
        context['extra_javascript'] = []
