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
    min_len = 1
    max_len = 6
    permute_value = CharField(required=True, min_length=min_len, max_length=max_len, strip=True, label="Value to Permute")

    def clean_permute_value(self):
        permute_value = self.cleaned_data.get('permute_value')

        # Just throw out any bad values
        permute_value = re.sub(r'\W+', '', permute_value)

        if len(permute_value) < self.min_len or len(permute_value) > self.max_len:
            raise ValidationError("{} to {} alphanumeric values are required.".format(str(self.min_len),
                                                                                      str(self.max_len)))

        return permute_value
