from django.shortcuts import render,redirect
from .models import Car
from .forms import carform
from django.contrib.auth.models import User

from django.contrib.auth import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    l=request.GET.get("name")
    print(l)
    context={
        'dict':Car.objects.all()
    }
    return render(request,'home.html',context)



@login_required(login_url='login')
def add_car(request):

    context={

        'db_form':carform()
    }

    if request.POST:
        carname=request.POST['carname']
        catagory=request.POST['catagory']
        discription=request.POST['discription']
        image=request.FILES['image']
        new=Car(carname=carname,catagory=catagory,discription=discription,image=image)
        new.save()

    return render(request,'addcar.html',context)





@login_required(login_url='login')
def update_car(request,id):
    temp=Car.objects.get(pk=id)
    new_carfrm = carform(instance=temp)

    if request.method == 'POST':
        new_carfrm=carform(request.POST,request.FILES,instance=temp)

        if new_carfrm.is_valid():
            new_carfrm.save()

            return redirect('home')

    return render(request,'update.html',{'up_frm':new_carfrm})




@login_required(login_url='login')
def delete_car(request,id):
    temp=Car.objects.get(pk=id)
    temp.delete()
    return redirect('home')



# ------------------authentication-----------------



def signup(request):
    user=None
    error_msg=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.create_user(username=username,password=password)
           
        except Exception as e:
            error_msg=str(e)

    return render(request,'signup.html',{'user':user,'error_msg':error_msg})


def user_login(request):
    err_msg=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
       
        if user:
            login(request,user)
            return redirect('home')
        else:
            err_msg='invalid user id'

    return render(request,'login.html',{'err_msg':err_msg})



def user_logout(request):

    logout(request)

    return redirect('home')
