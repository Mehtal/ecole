from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.


class Event(models.Model):
	user    = models.ForeignKey(User, on_delete=models.CASCADE , related_name='events')
	content = models.CharField(max_length=120)
	start   = models.DateField(auto_now=False, auto_now_add=False)
	end     = models.DateField(auto_now=False, auto_now_add=False)

	# def EventMessage(request):

	# 	qs = Event.objects.filter(start__lte=timezone.now().date(),end__gte=timezone.now().date(),user=request.user)
	# 	Event.objects.filter(end__lte=timezone.now().date()).delete()

	def __str__(self):
		return self.content