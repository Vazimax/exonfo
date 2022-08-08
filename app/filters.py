from dataclasses import field
import django_filters
from .models import * 
from django_filters import CharFilter

class OrderFilter(django_filters.FilterSet):
    english = CharFilter(lookup_expr='icontains')
    class Meta:
        model = PCWord
        fields = '__all__'
        exclude = ['field']
