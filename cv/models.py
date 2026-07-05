from django.db import models

class Education(models.Model):
    name_of_institution = models.CharField(max_length=50)
    start_year = models.IntegerField()
    finish_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name_of_institution