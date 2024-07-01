from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    age = models.IntegerField()
    image = models.CharField(max_length=500)
    def __str__(self):
        return self.name