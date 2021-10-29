from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render,redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,DetailView,ListView
from itertools import chain
from operator import attrgetter
from .models import User,Teacher,Student,Grade
from .forms import StudentSignUpForm,TeacherSignUpForm,UserForm,TeacherForm,StudentForm
from events.models import Event
from blog.models import Post
from marks.models import Marks






#@method_decorator(login_required, name='dispatch')
class HomeListView(ListView):
    template_name = 'accounts/home_list.html'
    context_object_name = 'list'


    def get_queryset(self):

        qs1 = "" #Marks.objects.filter(user=self.request.user)
      # qs2 = Event.objects.all()
        qs3 = Post.objects.all()
        queryset = sorted(
        chain(qs1,qs3),
        key=attrgetter('timestamp'),
        reverse=True)
        query = self.request.GET.get('q' , None)
        if query is not None :
            queryset = qs3.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) 
                )
        
        return queryset

    
'''
SIGN UP VIEWS FOR STUDENT AND TEACHERS

'''
class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'accounts/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')



'''
USER PROFILE VIEW FOR BOTH STUDENT/TEACHERS 
'''
@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    template_name = 'accounts/profile.html'
    queryset = User.objects.all() 
    
    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get('username'))


# class ProfileListView(ListView):
#     template_name = 'accounts/profile_list.html'
#     context_object_name = 'profile_list'
#     queryset = User.objects.all()
#     


'''
School Grade/Class List View 
'''
@method_decorator(login_required, name='dispatch')
class GradeDetailView(DetailView):
    template_name = 'accounts/grade.html'
    queryset = Grade.objects.all()

    def get_object(self):
        return get_object_or_404(Grade, name__iexact=self.kwargs.get('name'))






@login_required() 
def edit_profile(request, username):
    #querying User objects with username and Profile with id
    user = User.objects.get(username=username)
    if user.is_teacher:
        profile = Teacher.objects.get(id = user.teachers.id)
        profile_form = TeacherForm(instance=profile) 
    if user.is_student:
        profile = Student.objects.get(id = user.students.id)
        profile_form = StudentForm(instance=profile) 
        
    user_form = UserForm(instance=user)
       
    
    #making suer the user is authenticated and is the same user

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            if user.is_teacher:
                profile_form = TeacherForm(request.POST,request.FILES, instance=profile)
                user_form = UserForm(request.POST,request.FILES, instance=user)

            if user.is_student:
                profile_form = StudentForm(request.POST,request.FILES, instance=profile)
                user_form = UserForm(request.POST,request.FILES, instance=user)

            if profile_form.is_valid() and user_form.is_valid():
                created_profile = profile_form.save(commit=False)
                user_form.save()
                created_profile.save()              
                return redirect ('home' )

        return render (request, 'accounts/update.html', {"noodle": username,"noodle_form": user_form,"formset": profile_form})
    else:
        raise PermissionDenied

    