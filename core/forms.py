from django import forms

class YourForm(forms.Form):
    name = forms.CharField(max_length=100)
