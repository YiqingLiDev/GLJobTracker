from django.db import models
from django.forms import ModelForm

class mainJobList(models.Model):
    STATUS = (
        ('wishlist', 'wishlist'),
        ('applied', 'applied'),
        ('in progress', 'in progress'),
        ('offered', 'offered'),
        ('rejected', 'rejected')
    )

    status = models.CharField(max_length=200, choices=STATUS)
    job_title = models.CharField(max_length=200, null=True)
    company_name = models.CharField(max_length=200, null=True)
    applied_date = models.DateField()
    # deadline = models.DateField()
    # url_link = models.CharField(max_length=200, null=True)
    # note = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.company_name + ": " + self.job_title


class mainJobListForm(ModelForm):
    class Meta:
        model = mainJobList
        fields = "__all__"