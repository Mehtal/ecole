from django.db import models
from accounts.models import User 

# Create your models here.


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
	title = models.CharField(max_length=120)
	content = models.TextField(max_length=2000)
	image = models.ImageField(null=True, blank=True )
	draft = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	def __str__(self):
		return self.title


	class Meta:
		ordering = ["-updated","-timestamp" ,]
		verbose_name_plural = "Posts"