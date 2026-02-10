from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import MyUserCreationForm


def register(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("opportunities:list")
    else:
        form = MyUserCreationForm()

    return render(request, "registration/register.html", {"form": form})


def profile(request):
    return render(request, "profile.html")
