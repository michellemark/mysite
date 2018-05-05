"""
@Copyright Michelle Mark 2018
@author Michelle Mark

"""
from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from .models import ContactMe


class ContactMeForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget(), required=True)

    class Meta:
        model = ContactMe
        fields = ['your_name', 'message']
        widgets = {
            'your_name': forms.TextInput(attrs={'class': 'responsive-field'}),
            'message': forms.Textarea(attrs={'class': 'responsive-field'})
        }
