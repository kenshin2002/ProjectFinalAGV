from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = "<html><body>ManageAGV.</body></html>"
    return HttpResponse(html)