from django.shortcuts import render

def mainList(request):
    template = "dashboard/dashboard.html"

    
    return render(request, template)