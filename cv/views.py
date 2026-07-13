from django.http import HttpResponse
from django.shortcuts import render
from cv import models

def index(request):
    education_data = models.Education.objects.all()
    experience_data = models.Experience.objects.all()
    skills_data = models.Skills.objects.all()
    about_me_data = models.AboutMe.objects.all()
    certifications_data = models.Certifications.objects.all()
    projects_data = models.Projects.objects.all()
    volunteer_experience_data = models.VolunteerExperience.objects.all()

    data_dict = {
        "education_elements": education_data,
        "experience_elements": experience_data,
        "skill_elements": skills_data,
        "about_me_elements": about_me_data,
        "certifications_elements": certifications_data,
        "projects_elements": projects_data,
        "volunteer_experience_elements": volunteer_experience_data,
        }
    
    return render(request, "cv/home_page.html", data_dict)
