from django import forms
from .models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["title", "learningOutcome", "activityType", "timeSpent",
                  "cpdCredits", "practiceImpact"]
        error_messages = {
            'title': {
                'required': 'Please enter a title.'
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
        }