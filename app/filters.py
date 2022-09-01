from dataclasses import field
import django_filters
from .models import * 
from django_filters import CharFilter
from django.utils.translation import gettext_lazy
from django import forms

class OrderFilter(django_filters.FilterSet):
    english = django_filters.CharFilter(lookup_expr='icontains',label= gettext_lazy('English'),widget=forms.TextInput(attrs={'placeholder':'Search'}))
    french = django_filters.CharFilter(lookup_expr='icontains',label= gettext_lazy('French'),widget=forms.TextInput(attrs={'placeholder':'Chercher'}))
    arabic = django_filters.CharFilter(lookup_expr='icontains',label= gettext_lazy('Arabic'),widget=forms.TextInput(attrs={'placeholder':'ابحث'}))

    class Meta:
        model = PCWord
        fields = '__all__'
        exclude = ['field']
