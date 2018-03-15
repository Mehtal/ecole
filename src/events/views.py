from django.shortcuts import render
from django.utils import timezone
from .models import Event
# Create your views here.

def EventMessage(request):

	qs = Event.objects.filter(start__lte=timezone.now().date(),end__gte=timezone.now().date(),user=request.user)
	Event.objects.filter(end__lte=timezone.now().date()).delete()

	return render (request, 'navbar-loggedin.html', {'qs':qs})

