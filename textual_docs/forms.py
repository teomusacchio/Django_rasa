# forms.py

from django import forms
from django.forms import widgets


class TextualDocumentForm(forms.Form):
    titolo = forms.CharField(max_length=200)
    provenienza = forms.CharField(max_length=200)
    sezione = forms.CharField(max_length=200)
    sottosezione = forms.CharField(max_length=200)
    text_field = forms.CharField(widget=forms.Textarea)
    keywords = forms.CharField(max_length=200)
    summary = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=200)
    url = forms.URLField(required=False)
    document_type = forms.CharField(max_length=200)
    access_level = forms.CharField(max_length=200)
    tags = forms.CharField(max_length=200)
    # Assicurati di convertire i campi multi-valore come 'keywords' e 'tags' nel formato corretto
