from django.http import HttpResponse
from django.shortcuts import render
from .models import Education

def index(request):
    education_data = Education.objects.all()
    return render(request, "cv/home_page.html", {"education_elements": education_data})