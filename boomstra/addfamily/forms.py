from django import forms


class AddChildForm(forms.Form):
    name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
