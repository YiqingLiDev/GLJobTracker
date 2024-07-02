from django.shortcuts import render, redirect
from . import models
from . import filters

def mainList(request):
    template = "dashboard/dashboard.html"

    data = models.mainJobList.objects.all().order_by("-created_at")
    overall_applications = models.mainJobList.objects.count()
    progress_applications = models.mainJobList.objects.filter(status="in progress").count()

    form = models.mainJobListForm()

    if request.method == "POST":
        form = models.mainJobListForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    listFilter = filters.mainJobListFilter(request.GET, queryset=data) 
    data = listFilter.qs

    context = {'list': data,
               'form': form,
               'overall_applications': overall_applications,
               'progress_applications':progress_applications,
               'listFilter': listFilter,           
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


