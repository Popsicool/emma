from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User
from django.contrib.auth.models import auth
# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('transactions:dashboard')
        else:
            messages.info(request, 'Invalid Email or password')
            return redirect('authz:login')

    return render(request, "authz/login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        sex = request.POST['sex']
        country = request.POST['country']
        state_of_origin = request.POST['state_of_origin']
        address = request.POST['address']
        phone_num = request.POST['phone_num']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist")
                return redirect('authz:signup')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password,
                    date_of_birth= date_of_birth, sex = sex,country = country,phone_num=phone_num, state_of_origin = state_of_origin,address=address)
                user.save()
                messages.info(request, "Account created")
                return redirect('authz:login')
        else:
            messages.info(request, "Password didnt match")
            return redirect('authz:signup')
    return render(request, "authz/signup.html")
