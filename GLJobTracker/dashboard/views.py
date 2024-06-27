from django.shortcuts import render, redirect
from . import models

def mainList(request):
    template = "dashboard/dashboard.html"

    data = models.mainJobList.objects.all()

    form = models.mainJobListForm()

    if request.method == "POST":
        form = models.mainJobListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'list': data,
               'form': form,            
    }


    return render(request, template, context)