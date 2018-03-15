from django.shortcuts import render
from .models import Marks
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import MarksForm
from accounts.models import User,Teacher,Module
# Create your views here.


class MarksListView(ListView):
	model = Marks
	context_object_name = "marks"
	template_name = "marks_list.html"

class MarksCreateView(CreateView):

	model = Marks
	template_name = "marks_create.html"
	form_class = MarksForm
	success_url = reverse_lazy('home')

class MarksUpdateView(UpdateView):

	model = Marks
	template_name = "marks_update.html"
	form_class = MarksForm
	success_url = reverse_lazy('home')


def load_teachers(request):
	module_id= request.GET.get("module")
	teachers = Teacher.objects.filter(module_id=module_id)
	return render(request, 'teacher_dropdown_list_options.html', {'teachers': teachers})