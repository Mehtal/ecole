from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, RedirectView
from .models import Post, Image
from .forms import PostForm
from accounts.models import User
from accounts.models import Grade
from django.contrib import messages
import os
# Create your views here.

# class PostCreateView(CreateView):
#   model = Post
#   fields = ['user','title', 'content', 'image','draft',]
#   template_name = 'post_create.html'
#   success_url = reverse_lazy('blog:list')


@login_required(login_url='login')
def create_post(request):
    form = PostForm(request.POST, request.FILES,)
    images = request.FILES.getlist("images")
    print(images)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        for img in images:
            print(img)
            Image.objects.create(post=post, image=img)

        print(messages.success(request, "your post has been created sucessfully"))
        return redirect('home')
    return render(request, 'post_create.html', {'form': form})


class PostDetailView(DetailView):
    context_object_name = 'post'
    template_name = 'post_detail.html'
    queryset = Post.objects.all()

    def get_object(self):
        return get_object_or_404(Post, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        img_ext = ['.jpg', '.jpeg', '.png', '.svg']
        vid_ext = ['.mp4', '.avi']
        image_list = []
        vid_list = []
        file_list = []
        print("printing obj_list =======>", post.images.all())
        for obj in post.images.all():
            filename, file_extension = os.path.splitext(obj.image.url)
            if file_extension in img_ext:
                image_list.append(obj)
            if file_extension in vid_ext:
                vid_list.append(obj)
            if file_extension not in img_ext and file_extension not in vid_ext:
                file_list.append(obj)
            context['image_list'] = image_list
            context['vid_list'] = vid_list
            context['file_list'] = file_list
        return context


class PostLikeToggle(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

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

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            )
        return qs
    # queryset = Post.objects.all()


@login_required(login_url='login')
def PostUpdateView(request, pk):
    post = Post.objects.get(pk=pk)
    images = request.FILES.getlist("images")

    if not post.user == request.user:
        if not request.user.is_superuser:
            raise Http404
    form = PostForm(instance=post)
    if request.method == 'POST':
        if post.user == request.user or request.user.is_superuser:
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                # form = PostForm(request.POST , instance=post)
                post = form.save(commit=None)
                # post.user = request.user
                post.save()
                for img in images:
                    Image.objects.create(post=post, image=img)
                return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts_update_form.html', {'form': form, 'post': post, })


def image_delete(request, pk):
    img = Image.objects.get(id=pk)
    owner = img.post.user
    if request.user.is_superuser or request.user == owner:
        img.delete()
        messages.success(request, 'your file  was sucessfully deleted')
        return redirect("blog:detail", owner.id)
    else:
        messages.error(request, "you are not allowed to delet this item")
        return redirect("blog:detail", owner.id)
    return redirect('home')
