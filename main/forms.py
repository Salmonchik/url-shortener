from django import forms
from django.utils.translation import gettext_lazy as _


class URLShortenerForm(forms.Form):
    url = forms.CharField(
        max_length=2048,
        label='Your URL',
        help_text=_("The URL you want to shorten."),
        widget=forms.URLInput(
            attrs={
                'placeholder': 'https://www.example.com/',
                'required': 'true',
            },
        ),
    )
