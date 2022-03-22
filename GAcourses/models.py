from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128, unique=True)
    start_date = models.DateField()
    description = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name