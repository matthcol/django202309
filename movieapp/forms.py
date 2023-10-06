from django import forms

class MovieSearchForm(forms.Form):
    title = forms.CharField(
        label="Title", 
        min_length=1, 
        max_length=250,
        help_text="Enter movie title or just a part of it (case insensitive)",
        required=True
    )
    year = forms.IntegerField(
        label="Year",
        required=False
    )
