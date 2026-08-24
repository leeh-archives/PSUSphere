from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
