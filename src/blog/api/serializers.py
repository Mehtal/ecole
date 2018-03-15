from rest_framework import serializers
from blog.models import Post
from accounts.api.serializers import UserDisplaySerializer

class PostSerializer(serializers.ModelSerializer):
	# user = UserDisplaySerializer()
	class Meta:
		model = Post
		fields = [
		'pk',
		'user',
		'title',
		'content',
		'image',
		'updated',
		'timestamp',
		]
