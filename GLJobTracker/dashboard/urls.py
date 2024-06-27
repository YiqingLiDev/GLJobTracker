from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainList, name="maindashboard"),
    path('update_list/<int:pk>', views.update_list, name="update_list"),
]