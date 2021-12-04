from django.db import models
from accounts.models import User, Teacher, Module, Grade

# Create your models here.


class Grade(models.Model):
    niveau = (
        ('الإبتدائي', 'الإبتدائي'),
        ('المتوسط', 'المتوسط'),
        ('الثانوي', 'الثانوي'),
    )
    name = models.CharField(max_length=50, unique=True)
    level = models.CharField(max_length=30, choices=niveau, )

    def get_absolute_url(self):
        return reverse('grade:detail', args=[str(self.id)])

    def __str__(self):
        return self.name
