from django.urls import path, include
import manageAGV.views as views

urlpatterns = [
    path('', views.index)
]