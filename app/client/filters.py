import django_filters
from django_filters import CharFilter
from .models import Client
from django import forms


class ClienteFilter(django_filters.FilterSet):
    name = CharFilter(field_name='nome',
                      label='Nome',
                      lookup_expr='icontains',
                      widget=forms.TextInput(
                         attrs={"class": "form-control",
                                         'placeholder': 'Nome'}))
    surname = CharFilter(field_name='sobrenome',
                         lookup_expr='icontains',
                         label='Sobrenome',
                         widget=forms.TextInput(
                              attrs={"class": "form-control",
                                              'placeholder': 'Sobrenome'}))

    class Meta:
        model = Client
        fields = ['name', 'surname']


