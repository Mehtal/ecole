from django.conf.urls import url 
from django.views.generic.base import RedirectView
from blog import views

urlpatterns = [
	url(r'detail/(?P<pk>\d+)/like', views.PostLikeToggle.as_view(), name='like-toggle'),
	url(r'create/', views.create_post, name='create'),
    url(r'detail/(?P<pk>\d+)', views.PostDetailView.as_view(), name='detail'),

    url(r'update/(?P<pk>\d+)', views.PostUpdateView, name='update'),
    url(r'file/delete/(?P<pk>\d+)', views.image_delete, name='file-delete'),
    url(r'post/delete/(?P<pk>\d+)', views.post_delete, name='post-delete'),
    # url(r'', RedirectView.as_view(url="home")),

]