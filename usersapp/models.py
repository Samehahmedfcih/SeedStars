from django.db import models

# Create your models here.
class User(models.Model):
  Email=models.EmailField(unique= True)
  Name=models.CharField(max_length=20 )
  def __str__(self):
    return self.Name