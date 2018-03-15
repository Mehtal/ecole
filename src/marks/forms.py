from django import forms
from accounts.models import User,Teacher,Module
from .models import Marks


class MarksForm(forms.ModelForm):
	
	class Meta :
		model = Marks
		fields = ['user','module','teacher','grade']


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['teacher'].queryset = Teacher.objects.none()

		if 'module' in self.data:
			try:
				module_id = int(self.data.get('module'))
				self.fields['teacher'].queryset = Teacher.objects.filter(module_id=module_id)
			except (ValueError, TypeError):
				pass  # invalid input from the client; ignore and fallback to empty City queryset
		elif self.instance.pk:
			self.fields['teacher'].queryset = self.instance.module.teacher_set