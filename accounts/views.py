from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout

# Create your views here.
def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username!!')
            return redirect('/login-user/')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid password!!')
            return redirect('/login-user/')
        else:
            login(request, user)
            return redirect('/')


    return render(request, 'login_page.html')

def Register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already taken!!')
            return redirect('/register-user/')
        
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        messages.success(request, 'Your account created successfully!!')
        return redirect('/')


    return render(request, 'register.html')


def Logout_page(request):
    logout(request)
    return redirect('/login-user/')