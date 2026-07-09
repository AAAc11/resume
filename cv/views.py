from django.http import HttpResponse
from django.shortcuts import render
from .models import Education, Experience

def index(request):
    education_data = Education.objects.all()
    experience_data = Experience.objects.all()
    data_dict = {"education_elements": education_data, "experience_elements": experience_data}
    return render(request, "cv/home_page.html", data_dict)
