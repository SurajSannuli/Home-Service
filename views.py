from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from django.core.mail import send_mail
from .models import *
from .forms import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index(request):
    form=Servicemaster.objects.all()
    context = {'form':form}
    return render(request, 'index.html',context)
    
def viewlist(request):
    user_id = request.user
    u_id =user_id.id
    form = Serviceaddmaster.objects.filter(created_by=u_id)
    context = {'form':form,'u_id':u_id}
    return render(request,'view_list.html',context)
	
def Registerpage(request):
    form =CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request, 'Account was created '+user)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration.html',context)


def loginpage(request):
    if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('/book')
            else:
                messages.info(request,'Username or password Incorrect')
    return render(request, 'login.html')
 

def book(request):
    user_id = request.user  
    u_id=user_id.id
    form = PickForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = PickForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/viewlist')
    context = {'form':form,'u_id':u_id}
    return render(request, 'book.html',context)
		
		
		
def invoice(request,pk):
    form = Serviceaddmaster.objects.get(id=pk)
    context = {'form':form}
    return render(request,'invoice.html',context)
			

	