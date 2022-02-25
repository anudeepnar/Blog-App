from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from user.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success = (request, f'Hi {username}, your account was created successfully')
            return redirect('blog:home')
    else:

        form = UserRegisterForm()
    context = {
        'form': form
        }

    return render(request, 'user/register.html', context)

def user_login(request):
    
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('blog:home')

            else:
                return HttpResponse("Please use correct id and password")

    else:
        return render(request, "user/login.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))
