from django.shortcuts import render
from django.shortcuts import render
from .models import EmployeeForm,OfficeForm
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import redirect,render
from django.core import serializers
from django.forms.models import  model_to_dict
def home_view(request):
    officeForm = OfficeForm()
    employeeForm = EmployeeForm()
    context = {
        'officeForm':officeForm,
        'employeeForm':employeeForm
    }
    return render(request,'empapp/home.html',context)

# def 

def officeCrud(request):
    print(request.POST)
    # return redirect('')
    if request.method == "POST":
        officeForm = OfficeForm(request.POST)
        office = officeForm.save()
        body = office
        return JsonResponse(model_to_dict(office))
