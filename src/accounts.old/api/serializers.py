from rest_framework import serializers
from accounts.models import User


class UserDisplaySerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = [
		'username',
		'first_name',
		'last_name',
		'is_student',
		'is_teacher',
		]
