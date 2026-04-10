from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    progress = models.CharField(max_length=50)

class Worker(models.Model):
    name = models.CharField(max_length=100)
    task = models.CharField(max_length=100)

class Material(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

from django.db import models

class Budget(models.Model):
    amount = models.IntegerField() 
    desc = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.amount} - {self.desc}"