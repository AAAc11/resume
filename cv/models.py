from django.db import models

class Education(models.Model):
    name_of_institution = models.CharField(max_length=50)
    start_year = models.IntegerField()
    finish_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_of_institution
    

class Experience(models.Model):
    employer = models.CharField(max_length=50)
    position_held_at_work = models.CharField(max_length=50)
    place_of_work = models.CharField(max_length=50)
    start_date = models.DateField()
    finish_date = models.DateField()
    work_description = models.TextField(max_length=400)


    def __str__(self):
        return self.employer
    