from rest_framework import generics , mixins
from blog.models import Post
from .serializers import PostSerializer
from django.db.models import Q


class PostAPIView(mixins.CreateModelMixin ,generics.ListAPIView):
	
	lookup_fields 		= 'pk'
	serializer_class	= PostSerializer

	def get_queryset(self):
		qs = Post.objects.all()
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
		return qs

	def perfom_create(self, serializer):
		return serializer.save(user.self.request.user)

	def post (self, request, *args , **kwargs):
		return self.create(request, *args, **kwargs)


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
	
	lookup_fields 		= 'pk'
	queryset			= Post.objects.all()
	serializer_class	= PostSerializer