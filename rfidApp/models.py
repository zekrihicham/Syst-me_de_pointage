from django.db import models

# Create your models here.


class Utlisateur(models.Model):
    rfid = models.IntegerField(unique=True)
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)


class Presence(models.Model):
    user = models.ForeignKey(Utlisateur,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,blank=True)

