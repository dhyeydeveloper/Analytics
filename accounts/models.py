from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=225)
    position = models.CharField(max_length=225)
    office = models.CharField(max_length=225)
    age = models.IntegerField()
    joining_date = models.DateField(null=True)
    salary = models.IntegerField()