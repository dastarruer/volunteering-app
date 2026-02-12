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


def opportunity(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    return render(request, "opportunity.html", {"opportunity": opportunity})
