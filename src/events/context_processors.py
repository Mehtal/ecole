from events.models import Event
from django.utils import timezone


def EventMessage(request):
	qs = Event.objects.all()
	if request.user.is_authenticated() :
		qs = Event.objects.filter(start__lte=timezone.now().date(),end__gte=timezone.now().date(),user=request.user)
		Event.objects.filter(end__lte=timezone.now().date()).delete()

	return {'events': qs}