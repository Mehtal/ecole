from django.db import models
from accounts.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
import os
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=120)
    content = RichTextField(config_name='awesome_ckeditor',blank=True,null=True,max_length=2000)
    like = models.ManyToManyField(User, related_name="likes", blank=True,)
    draft = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.id)])

    def get_like_url(self):
        return reverse('blog:like-toggle', args=[str(self.id)])

    def get_like_api_url(self):
        return reverse("api_blog:like-api-toggle", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated", "-timestamp", ]
        verbose_name_plural = "Posts"


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    post = models.ForeignKey(
        Post, related_name="images", on_delete=models.CASCADE,)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.id)])

    def filename(self):
        return os.path.basename(self.image.name)

    def __str__(self):
        return self.post.title
    # width = models.FloatField(default=100)
    # length = models.FloatField(default=100)
