from django.db import models

class Education(models.Model):
    institution_name = models.CharField(max_length=100)
    start_year = models.IntegerField()
    finish_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_of_institution
    

class Experience(models.Model):
    employer = models.CharField(max_length=100)
    position_held_at_work = models.CharField(max_length=100)
    place_of_work = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()
    work_description = models.TextField(max_length=1000)


    def __str__(self):
        return self.employer
    
class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    category_choices = [
        ("Cognitive skills", "Cognitive skills"),
        ("Technical skills", "Technical skills"),
        ("Creative skills", "Creative skills"),
        ("Managment skills", "Managment skills"),
    ]
    skill_category = models.CharField(choices=category_choices)

    def __str__(self):
        return self.skill_name
    
class AboutMe(models.Model):
    about_me_description = models.TextField(max_length=2000)

    def __str__(self):
        return self.about_me_description
    
class Certifications(models.Model):
    certification_name = models.CharField(max_length=100)
    issuing_institution = models.CharField(max_length=100)
    date_of_issue = models.DateField()
    gained_skills = models.CharField(blank=True, null=True)
    certification_description = models.TextField(max_length=1000)
    credential_ID = models.CharField(max_length=100)

    def __str__(self):
        return self.certification_name

class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField(max_length=2000)
    creators = models.CharField(max_length=200, blank=True, null=True)
    used_tools = models.TextField(max_length=500)
    start_date = models.DateField()
    finish_date = models.DateField()
    project_link = models.URLField()

    def __str__(self):
        return self.project_name
    
class VolunteerExperience(models.Model):
    volunteer_role = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=100)
    volunteering_start_date = models.DateField()
    volunteering_finish_date = models.DateField()
    description_of_volunteering = models.TextField(max_length=1000)

    def __str__(self):
        return self.volunteer_role