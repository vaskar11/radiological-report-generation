from django.db import models

# Create your models here.

class doctor(models.Model):
    doctor_image= models.ImageField()
    doctor_name= models.CharField(max_length=100)
    doctor_spec= models.CharField(max_length=200,default= 'physician')
    doctor_details= models.TextField()
    
    def __str__(self):
        return self.doctor_name