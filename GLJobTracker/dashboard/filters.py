import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import *

class mainJobListFilter(django_filters.FilterSet):

    # custom attribute
    start_date = DateFilter(field_name="created_at", lookup_expr="gte")
    end_date = DateFilter(field_name="created_at", lookup_expr="lte")

    year = NumberFilter(field_name="applied_date", lookup_expr="year")

    company_name = CharFilter(field_name="company_name", lookup_expr="icontains")
    job_title = CharFilter(field_name="job_title", lookup_expr="icontains")


    class Meta:
        model = mainJobList
        fields = '__all__'
        # fields = []
        exclude = ['created_at']


    # # filter the primary queryset
    # @property
    # def qs(self):

        # parent = super().qs # obtain the original queryset before applying aditional filitering
        # # print("Parent QS:", parent)  # Debugging line! Learned from Bo

        # # It can also limit the "user"

        # return parent.filter(status="wishlist")