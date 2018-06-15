"""
@Copyright Michelle Mark 2018
@author Michelle Mark

"""
import re

from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, Form, CharField
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

from .models import ContactMe


class ContactMeForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget(), required=True)

    class Meta:
        model = ContactMe
        fields = ['your_name', 'message']
        widgets = {
            'your_name': TextInput(attrs={'class': 'responsive-field'}),
            'message': Textarea(attrs={'class': 'responsive-field'})
        }


class PermuteForm(Form):
    permute_value = CharField(required=True, min_length=1, max_length=6, strip=True, label="Value to Permute")

    def clean_permute_value(self):
        permute_value = self.cleaned_data.get('permute_value')

        # Just throw out any bad values
        permute_value = re.sub(r'\W+', '', permute_value)

        if len(permute_value) == 0:
            raise ValidationError("1 to 4 alphanumeric values are required.")

        return permute_value
