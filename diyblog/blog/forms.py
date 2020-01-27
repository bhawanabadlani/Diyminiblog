import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AddComment(forms.Form):
    added_comment = forms.CharField(help_text="Add a comment")

    def clean_comment(self):
        data = self.cleaned_data['added_comment']

        # Remember to always return the cleaned data.
        return data