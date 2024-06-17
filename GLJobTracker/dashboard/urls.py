from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainList, name="maindashboard")
]