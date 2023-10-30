# textual_docs/urls.py

from django.urls import path
from .views import add_textual_document  # assicurati di importare la tua vista
from .views import success_view
urlpatterns = [
    path('add/', add_textual_document, name='add_textual_document'),
    path('success/', success_view, name='success'),  # Aggiungi questo
]
