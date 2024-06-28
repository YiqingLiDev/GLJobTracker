from django.shortcuts import render, redirect
from . import models

def mainList(request):
    template = "dashboard/dashboard.html"

    data = models.mainJobList.objects.all()
    overall_applications = models.mainJobList.objects.count()

    form = models.mainJobListForm()

    if request.method == "POST":
        form = models.mainJobListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context = {'list': data,
               'form': form,
               'overall_applications': overall_applications,            
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

def delete_list(request, pk):
    template = 'dashboard/delete_list.html'

    data = models.mainJobList.objects.get(id = pk)

    if request.method == "POST":
        data.delete()
        return redirect('/')

    context = {'list': data}

    return render(request, template, context)


