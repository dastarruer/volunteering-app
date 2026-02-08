from django.shortcuts import get_object_or_404, render

from .models import Opportunity


# Create your views here.
def opportunities(request):
    opportunities = Opportunity.objects.all()
    return render(request, "list.html", {"opportunities": opportunities})


def opportunity(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk)
    return render(request, "opportunity.html", {"opportunity": opportunity})
