from django.db import models

# Create your models here.
class halls(models.Model):
    hall_id = models.BigAutoField(primary_key=True)
    hall_img = models.ImageField(upload_to='images/')
    hall_name=models.CharField(max_length=50)
    hall_mem=models.IntegerField()
    def __str__(self):
        return self.hall_name
    
class Register(models.Model):
    uname=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.uname
class booking(models.Model):
    uname=models.CharField(max_length=50)
    hall_name=models.CharField(max_length=50)
    hall_mem=models.IntegerField()
    dept=models.CharField(max_length=50)
    eventname=models.CharField(max_length=100)
    coordinatename=models.CharField(max_length=50)
    coordinateid=models.CharField(max_length=20)
    totalmember=models.IntegerField()
    date=models.DateField()
    time=models.CharField(max_length=80)
    def __str__(self):
        return self.hall_name