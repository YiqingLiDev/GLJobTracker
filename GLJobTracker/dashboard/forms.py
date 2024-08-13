from django.forms import ModelForm
from django import forms
from GLJobTracker import settings
from . import models

class mainJobListForm(ModelForm):
    # applied_date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = models.mainJobList
        fields = "__all__"