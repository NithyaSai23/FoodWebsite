from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('display/',views.display,name='display'),
    path('add/',views.add,name='add'),
    path('change/',views.change,name='change'),
    path('change/delete/<foodid>',views.delete,name="delete"),
    path('change/update/<foodid>',views.update,name="update"),
    path('change/update/updaterecord/<foodid>',views.updaterecord,name="updaterecord")
   
]