from django.db import models

# Create your models here.
class patient(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    phone=models.CharField(max_length=100)
    disease=models.TextField()
    admission_date=models.DateField()
    
    def __str__(self):
        return self.name