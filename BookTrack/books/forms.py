from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(
        label='Search',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        # validators=[alphanumeric]
    )
