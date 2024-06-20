from django.shortcuts import render
from . import models

def mainList(request):
    template = "dashboard/dashboard.html"

    data = models.mainJobList.objects.all()

    forms = models.mainJobListForm()

    context = {'list': data,
               'form': forms,            
    }


    return render(request, template, context)