from rest_framework import generics , mixins
from blog.models import Post
from .serializers import PostSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.shortcuts import render , redirect , get_object_or_404

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




class PostLikeAPIToggle(APIView):
  
	authentication_classes = (authentication.SessionAuthentication,)
	permission_classes = (permissions.IsAuthenticated,)

	def get(self, request,pk=None, format=None):

		obj = get_object_or_404(Post, pk=self.kwargs['pk'])
		url_ = obj.get_absolute_url() 
		user = self.request.user
		updated = False
		liked = False
		if user.is_authenticated():
			if user in obj.like.all():
				liked = False
				obj.like.remove(user)
			else:
				liked = True
				obj.like.add(user)
			updated = True
		data = {
			"updated": updated,
			"liked": liked,
		}
		return Response(data)