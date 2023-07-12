from django.shortcuts import render
from django.shortcuts import render
from .models import EmployeeForm,OfficeForm
# Create your views here.

def home_view(request):
    officeForm = OfficeForm()
    employeeForm = EmployeeForm()
    context = {
        'officeForm':officeForm,
        'employeeForm':employeeForm
    }
    return render(request,'empapp/home.html',context)

# def 