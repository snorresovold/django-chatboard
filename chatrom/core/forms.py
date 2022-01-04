from django import forms

class CreateNewPost(forms.Form):
    name = forms.CharField(max_length=255)
    content = forms.CharField(max_length=1000)