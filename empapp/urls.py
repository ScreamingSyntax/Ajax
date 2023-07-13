from django.urls import path
from empapp.views import home_view
from empapp.views import *

urlpatterns = [
    path('',home_view,name='home'),
    path('office/',officeCrud,name='crud'),
    path('emp/',empCrud,name='emp'),
    path("offices/",getAllOffices,name="officeall")
]