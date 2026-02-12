from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import MyUserCreationForm
from .models import User
from django.contrib.auth.decorators import login_required


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


@login_required
def profile(request):
    upcoming_opportunities = request.user.upcoming_opportunities.all()

    context = {
        "upcoming_opportunities": upcoming_opportunities,
    }
    return render(request, "profile.html", context)
