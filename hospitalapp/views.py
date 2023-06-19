from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Appointment,AllAppointments
import re

# Create your views here.


def HomePage(request):
    return render(request,'index.html')

def admin_view(request):
    return render(request,'adminpage.html')

def patient_view(request):
    return render(request,'patientpage.html')

def admin_signup_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',pass1)

        if password is None:
            context={'message1':'Your password must be 8 characters and it must contain combination of one Uppercase,lowercase,digits and special characters.'}
            return render(request,'admin_signup.html',context)
        else:
            if pass1!=pass2:
                context = {'message':'Password and Confirm password are not matching'}
                return render(request,'admin_signup.html',context)
            else:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.is_active = True
                my_user.first_name = first_name
                my_user.last_name = last_name
                my_user.save()
                return redirect('admin')
    return render(request,'admin_signup.html')


def admin_login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('admin_dashboard')
        else:
            context = {'message':'Username and Password are incorrect !!!'}
            return render(request,'admin_login.html',context)
    return render(request,'admin_login.html')

def patient_signup_view(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = re.match('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',pass1)

        if password is None:
            context={'message1':'Your password must be 8 characters and it must contain combination of one Uppercase,lowercase,digits and special characters.'}
            return render(request,'admin_signup.html',context)
        else:
            if pass1!=pass2:
                context = {'message':'Password and Confirm password are not matching'}
                return render(request,'patient_signup.html',context)
            else:
                my_user=User.objects.create_user(uname,email,pass1)
                my_user.is_active = True
                my_user.first_name = first_name
                my_user.last_name = last_name
                my_user.save()
                return redirect('patient')
    return render(request,'patient_signup.html')

def patient_login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('patient_dashboard')
        else:
            context = {'message':'Username and Password are incorrect !!!'}
            return render(request,'patient_login.html',context)
    return render(request,'patient_login.html')

def admin_dashboard(request):
    user_name = request.user.first_name
    appointment = Appointment.objects.all()
    return render(request,'admin_dashboard.html',{'user':user_name,'appointment':appointment})

def patient_dashboard(request):
    user_name = request.user.first_name
    return render(request,'patient_dashboard.html',{'user':user_name})


def patient_appointment(request):
    if request.method == 'GET':
        user_name = request.user.first_name
        return render(request,'patient_appointment.html',{'user':user_name})
    else:
        Appointment(
            name = request.POST['name'],
            age = request.POST['age'],
            gender  =request.POST['gender'],
            blood_group = request.POST['blood_group'],
            address = request.POST['address'],
            city = request.POST['city'],
            branch = request.POST['branch'],
            date = request.POST['date']
        ).save()
        AllAppointments(
            name = request.POST['name'],
            age = request.POST['age'],
            gender  =request.POST['gender'],
            blood_group = request.POST['blood_group'],
            address = request.POST['address'],
            city = request.POST['city'],
            branch = request.POST['branch'],
            date = request.POST['date']
        ).save()
        return redirect('patient_dashboard')
    
def appointment_reject(request,id):
    data = Appointment.objects.get(id=id)
    data1 = AllAppointments.objects.get(id=id)
    data1.status = -1
    data1.save()
    data.delete()
    return redirect('admin_dashboard')

def appointment_accept(request,id):
    data = Appointment.objects.get(id=id)
    data1 = AllAppointments.objects.get(id=id)
    data.status = 1
    data1.status = 1
    data.save()
    data1.save()
    return redirect('admin_dashboard')

def check_status(request):
    name1 = request.user.first_name
    data = AllAppointments.objects.get(name=name1)
    stat = data.status
    date = data.date
    return render(request,'status.html',{'status':stat,'date':date,'data':data})

def admin_logout_view(request):
    logout(request)
    return redirect('admin')

def patient_logout_view(request):
    logout(request)
    return redirect('patient')

