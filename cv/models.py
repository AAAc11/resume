from django.db import models

class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField(max_length=800)
    technologies = models.CharField(max_length=100, blank=True)
    project_link = models.URLField()
    display_order = models.IntegerField(default=0)

    def __str__(self):
        return self.project_name
    