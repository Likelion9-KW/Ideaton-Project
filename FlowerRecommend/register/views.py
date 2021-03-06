from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from register.forms import MyAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

def join_view(request):
    if request.method == 'POST':
        print(request.POST['username'])
        print(request.POST['nickname'])

        form = MyAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("main")
        else:
            print(form.errors)
            return redirect("main")
    else:
        print("star")
        form = MyAuthenticationForm()
        return render(request, "join.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request=request, username=username, password=password)
            if user is not None:

                login(request, user)
                return redirect("main")
            else:
                return redirect("login")

    form = AuthenticationForm()
    return render(request, "login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect("main")
