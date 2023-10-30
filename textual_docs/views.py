# views.py

from django.shortcuts import render, redirect
from django.conf import settings
from .forms import TextualDocumentForm
from elasticsearch import Elasticsearch


def success_view(request):
    # Assicurati di avere un template 'success.html' nella cartella dei template.
    return render(request, 'success.html')


def add_textual_document(request):
    # Crea una istanza del client Elasticsearch con i dettagli del server.
    es = Elasticsearch([{
        'host': settings.ELASTICSEARCH_HOST,
        'port': settings.ELASTICSEARCH_PORT,
        'scheme': getattr(settings, 'ELASTICSEARCH_SCHEME', 'http')
    }])

    if request.method == 'POST':
        form = TextualDocumentForm(request.POST)
        if form.is_valid():
            # Index il documento valido in Elasticsearch
            es.index(index="documentazione_testuale", body=form.cleaned_data)
            # Reindirizza alla vista di successo, assicurati che 'success' sia definito in urls.py
            return redirect('success')
    else:
        form = TextualDocumentForm()

    return render(request, 'add_textual_document.html', {'form': form})
