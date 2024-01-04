from django.db import models

# Create your models here.
class college(models.Model):
    college_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=20)
    about=models.TextField()
    type=models.CharField(max_length=50,choices=(('Technical','Technical'),('Non-technical','Non-techincal'),('Both','Both')))
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    phone_no=models.CharField(max_length=10)
    about=models.TextField()
    
College=models.ForeignKey(college, on_delete=models.CASCADE)
