from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=100)
    task = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Budget(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    desc = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)

    def __str__(self):
        if self.project:
            return f"{self.project.name} - {self.desc} - ₹{self.amount}"
        return f"{self.desc} - ₹{self.amount}"

    class Meta:
        unique_together = ('project', 'desc')