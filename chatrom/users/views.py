from django.shortcuts import render, redirect
from django.contrib.auth import login

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .forms import RegisterForm

# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        fields = RegisterForm().fields
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")

    else:
        form = RegisterForm()
        fields = RegisterForm().fields
    return render(request, "user/register.html", {"form":form, "fields":fields})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        fields = AuthenticationForm().fields
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")

    else:
        form = AuthenticationForm()
        fields = AuthenticationForm().fields
    return render(request, "registration/login.html", {'form': form, 'fields': fields})