from django.db import models
from django.forms import ModelForm
# Create your models here.
class Office(models.Model):
    """Class representing a office"""
    name= models.CharField(max_length=50)
    location= models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

 
class Employee(models.Model):
    """Class representing a Employee"""
    genders = [
        ("M","Male"),
        ("F","Female")
    ]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20,choices=genders)
    office = models.ForeignKey(Office,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name +" "+self.last_name


class OfficeForm(ModelForm):
    class Meta:
        model = Office
        fields = "__all__"

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
