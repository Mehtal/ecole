from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render , redirect , get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView , ListView , UpdateView,CreateView ,RedirectView
from .models import Post
from .forms import PostForm
from accounts.models import  User
from accounts.models import Grade



# Create your views here.

# class PostCreateView(CreateView):
# 	model = Post 
# 	fields = ['user','title', 'content', 'image','draft',]
# 	template_name = 'post_create.html'
# 	success_url = reverse_lazy('blog:list')

@login_required(login_url='login')
def create_post(request):
	form = PostForm(request.POST,request.FILES,)
	if form.is_valid():
		post = form.save(commit=False)
		post.user = request.user
		post.save()
		return redirect('home')
	return render(request, 'post_create.html', {'form':form})




class PostDetailView(DetailView):
	context_object_name = 'post'
	template_name = 'post_detail.html'
	queryset = Post.objects.all()

	def get_object(self):
		return get_object_or_404(Post, pk=self.kwargs['pk'])

class PostLikeToggle(RedirectView):

	def get_redirect_url(self, *args ,**kwargs):
		
		obj = get_object_or_404(Post, pk=self.kwargs['pk'])
		url_ = obj.get_absolute_url() 
		user = self.request.user
		if user.is_authenticated():
			if user in obj.like.all():
				obj.like.remove(user)
			else:
				obj.like.add(user)

		return url_


	pass


class PostListView(ListView):
	template_name = 'post_list.html'
	context_object_name = 'posts'

	def get_queryset(self, *args , **kwargs):
		qs = Post.objects.all()
		query = self.request.GET.get('q' , None)
		if query is not None :
			qs = qs.filter(
				Q(title__icontains=query) |
				Q(content__icontains=query) 
				)
		return qs 
	# queryset = Post.objects.all()

@login_required(login_url='login')
def PostUpdateView(request, pk):
	post = Post.objects.get(pk=pk)
	if not post.user == request.user :
		raise Http404
	form = PostForm(instance=post)
	if request.method == 'POST' and  post.user == request.user:
		form = PostForm(request.POST,request.FILES, instance=post)
		if form.is_valid():
			# form = PostForm(request.POST , instance=post)
			post = form.save(commit=None)
			# post.user = request.user
			post.save()
			return redirect('home')
	else:
		form = PostForm(instance=post)

	return render(request, 'posts_update_form.html', {'form':form})



