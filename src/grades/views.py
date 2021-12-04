from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView, RedirectView
from .models import Grade
# Create your views here.


class GradeDetailView(DetailView):
    model = Grade
    context_object_name = 'grade'
    template_name = 'grades/grade_detail.html'


class PostListView(ListView):
    template_name = 'grades/grade_list.html'
    context_object_name = 'grades'
    queryset = Grade.objects.all()
