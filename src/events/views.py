from django.shortcuts import render
from django.utils import timezone
from .models import Event
from django.views.generic.edit import CreateView
from django.urls import reverse

# Create your views here.

def EventMessage(request):

	qs = Event.objects.filter(start__lte=timezone.now().date(),end__gte=timezone.now().date(),user=request.user)
	Event.objects.filter(end__lte=timezone.now().date()).delete()

	return render (request, 'navbar-loggedin.html', {'qs':qs})

class EventCreate(CreateView):
    model = Event
    fields = ['user','content','start','end']
    success_url="/"
    # template_name = "accounts/right-section.html"