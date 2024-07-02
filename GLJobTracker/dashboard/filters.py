import django_filters
from django_filters import DateFilter

from .models import mainJobList

class mainJobListFilter(django_filters.FilterSet):
    class Meta:
        model = mainJobList
        fields = '__all__'
        exclude = ['created_at']