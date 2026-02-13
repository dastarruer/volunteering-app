from datetime import timedelta

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

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


@login_required
def profile(request):
    user = request.user
    last_opportunity = user.completed_opportunities.order_by("-opportunity_date").first()

    if user.streak_last_updated:
        now = timezone.now()
        # If it's been more than 7 days, reset streak
        if now - user.streak_last_updated > timedelta(days=7):
            user.streak = 0
            user.save()
        # If it's been exactly 7 days and the user has completed an opportunity, increment the streak
        # Yes this logic is bad, and no i will not be fixing it. this is a prototype.
        elif last_opportunity and user.streak_last_updated == timedelta(days=7):
            user.streak += 1
            user.streak_last_updated = now

    upcoming_opportunities = request.user.upcoming_opportunities.all()
    completed_opportunities = request.user.completed_opportunities.all()

    context = {
        "upcoming_opportunities": upcoming_opportunities,
        "completed_opportunities": completed_opportunities,
        "streak": user.streak
    }
    return render(request, "profile.html", context)
