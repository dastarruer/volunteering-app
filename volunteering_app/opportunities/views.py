from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

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

    # Check if the user has signed up for the current opportunity
    is_signed_up = (
        request.user.upcoming_opportunities.filter(id=pk).exists()
        or request.user.completed_opportunities.filter(id=pk).exists()
    )

    context = {"opportunity": opportunity, "is_signed_up": is_signed_up}

    return render(request, "opportunity.html", context)
