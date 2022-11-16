from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm
# Create your views here.
from .models import *

#from .filters import OrderFilter

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
            

        context = {'form':form}
        return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
    

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'dashboard.html')
"""
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
    'total_orders':total_orders,'delivered':delivered,
    'pending':pending }
    """
@login_required(login_url='login')
def wallect(request):
    wallect = wallect.objects.all()

    return render(request, 'wallect.html', {'wallect':wallect})

@login_required(login_url='login')
def send_money(request):
    #send_money= send_money.objects.all()
     
      return render(request, 'send_money.html',{'send_money':send_money})

@login_required(login_url='login')
def Request_money(request):
    #send_money= send_money.objects.all()
     
      return render(request, 'request_money.html',{' Request_money': Request_money})

@login_required(login_url='login')
def Request_Recived(request):
    #send_money= send_money.objects.all()
     
      return render(request, 'Request_Recived.html',{'Request_Recived': Request_Recived})