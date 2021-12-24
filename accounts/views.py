from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm
from django.urls import reverse


# Create your views here
# 
# .
def dashboard(request):
    return render(request, "accounts/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "register.html",
            {"form": RegisterForm}
        )
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

