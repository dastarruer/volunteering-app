from django.shortcuts import render
from .models import Opportunity


# Create your views here.
def opportunities(request):
    opportunities = Opportunity.objects.all()
    return render(request, "list.html", {"opportunities": opportunities})
