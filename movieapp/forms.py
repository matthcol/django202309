from django import forms

class MovieSearchForm(forms.Form):
    title = forms.CharField(
        label="Title", 
        min_length=1, 
        max_length=250)
