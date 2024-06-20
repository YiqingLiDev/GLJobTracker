from django.shortcuts import render
from . import models

def mainList(request):
    template = "dashboard/dashboard.html"

    data = models.mainJobList.objects.all()

    context = {'list': data}


    return render(request, template, context)