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


def update_list(request, pk):
    template = 'dashboard/update_list.html'

    data = models.mainJobList.objects.get(id = pk)
    form = models.mainJobListForm(instance = data)

    if request.method == "POST":
        form = models.mainJobListForm(request.POST, instance = data)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}

    return render(request, template, context)
