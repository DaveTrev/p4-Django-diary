from django import forms
from .models import Entry
from django.core.validators import MinValueValidator


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["title", "learningOutcome", "activityType", "timeSpent",
                  "cpdCredits", "practiceImpact"]
        error_messages = {
            'title': {
                'required': 'Please enter a title.'
            },
            'timeSpent': {
                'required': 'Please enter the amount of time spent.'
            },
            'learningOutcome': {
                'required': 'Please enter details of your learning outcome.'
            },
            'activityType': {
                'required': 'Please enter the type of learning activity.'
            },
            'practiceImpact': {
                'required': 'Please enter the impact on your practice.'
            },
            'cpdCredits': {
                'required': 'Please enter the amount of CPD claimed.'
            },
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'required': True, 'placeholder':
                                            'Enter a Title'}),
            'learningOutcome': forms.Textarea(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder': 'Enter details on your learning.'}),
            'activityType': forms.Textarea(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder': 'Enter the type of activity.'}),
            'practiceImpact': forms.Textarea(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder':
                       'Enter details on the impact on your practice.'}),
            'timeSpent': forms.TextInput(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder': 'e.g. 3 hours'}),
            'cpdCredits': forms.NumberInput(
                attrs={'class': 'form-control', 'required': True,
                       'placeholder': 'Enter CPD Credits Claimed'}
            ),
        }
