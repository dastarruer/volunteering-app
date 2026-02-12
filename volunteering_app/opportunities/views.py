from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import F

from .models import Opportunity


# Create your views here.
@login_required
def opportunities(request):
    signed_up_ids = request.user.upcoming_opportunities.values_list("id", flat=True)
    completed_ids = request.user.completed_opportunities.values_list("id", flat=True)
    excluded_ids = list(signed_up_ids) + list(completed_ids)

    # Only show opportunities that the user has not signed up for or completed
    opportunities = Opportunity.objects.exclude(id__in=excluded_ids)

    return render(request, "list.html", {"opportunities": opportunities})


@login_required
def opportunity(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    is_upcoming = request.user.upcoming_opportunities.filter(id=pk).exists()  #
    is_completed = request.user.completed_opportunities.filter(id=pk).exists()

    # Check if the user has signed up for the current opportunity
    is_signed_up = is_upcoming or is_completed

    if request.method == "POST":
        if is_upcoming:
            request.user.upcoming_opportunities.remove(opportunity)
            opportunity.num_signed_volunteers = F("num_signed_volunteers") - 1
            opportunity.save()
        elif not is_completed:
            request.user.upcoming_opportunities.add(opportunity)
            opportunity.num_signed_volunteers = F("num_signed_volunteers") + 1
            opportunity.save()

        return redirect("opportunities:opportunity", pk=pk)

    context = {"opportunity": opportunity, "is_signed_up": is_signed_up}

    return render(request, "opportunity.html", context)
