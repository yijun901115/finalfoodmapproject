from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import SignupForm

# Create your views here.


def signUp(request):
    if request.user.is_anonymous:
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect("memberaccountnewuser:signin")
    else:
        return redirect("memberaccountnewuser:signup")

    form = SignupForm()
    context = {
        'form': form
    }
    return render(request, "signUpPage.html", context)


def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('homepage')
    return render(request, "signInPage.html",)


def account_logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
