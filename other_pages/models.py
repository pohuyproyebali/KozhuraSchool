from django.db import models


# Create your models here.


class ApplicationFromEmployer(models.Model):
    employer_name = models.CharField(max_length=100)
    employer_email = models.EmailField(max_length=100)
    employer_phone = models.CharField(max_length=100)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employer_name
