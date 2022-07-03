from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from matplotlib.style import context
from .models import Item
from .forms import Itemform
# Create your views here.
def index(request):
    return render(request,'index.html')
def display(request):
    mymembers=Item.objects.all().values()
    #print(items)
    return render(request,'display.html',{'mymembers':mymembers})
def delete(request,foodid):
    m=Item.objects.get(foodid=foodid)
    m.delete()
    return HttpResponseRedirect(reverse('display'))
def change(request):
    mymembers=Item.objects.all().values()
    #print(items)
    return render(request,'deleteorupdate.html',{'mymembers':mymembers})
def add(request):
    
    
    if request.method=='POST':
        form=Itemform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('display'))
    else:
        form=Itemform()
        context={'form':form}
        return render(request,'add.html',context)
def update(request,foodid):
    m=Item.objects.get(foodid=foodid)
   

    con={
        'item':m,
        
    }
    return render(request,'update.html',con)
def updaterecord(request,foodid):
    m=Item.objects.get(foodid=foodid)
    c=request.POST['cost']
    print("dhfsl")
    m.cost=c
    m.save()
    return HttpResponseRedirect(reverse('display'))