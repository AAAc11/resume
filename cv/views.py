from django.http import HttpResponse
from django.shortcuts import render
from .models import Projects

def index(request):
    projects_data = Projects.objects.all().order_by('display_order')
    
    return render(request, "cv/home_page.html", {'projects': projects_data})
