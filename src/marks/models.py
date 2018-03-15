from django.db import models
from accounts.models  import User,Teacher,Module,Grade

# Create your models here.

class Marks(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	module = models.ForeignKey(Module, on_delete=models.CASCADE) # will change it later to choice_Field
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,)
	grade = models.IntegerField()
	date = models.DateField(auto_now=False, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True,)

	def __str__(self):
		return self.user.first_name + " " + self.user.last_name

	class Meta:
		ordering = ["-timestamp" ,]