from django import forms

class TaskForm(forms.Form):
    name = forms.CharField()
    is_active = forms.BooleanField()