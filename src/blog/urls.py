from django.conf.urls import url 
from django.views.generic.base import RedirectView
from blog import views

urlpatterns = [
	url(r'detail/(?P<pk>\d+)/like', views.PostLikeToggle.as_view(), name='like-toggle'),
	url(r'create/', views.create_post, name='create'),
    url(r'detail/(?P<pk>\d+)', views.PostDetailView.as_view(), name='detail'),

    url(r'update/(?P<pk>\d+)', views.PostUpdateView, name='update'),
    # url(r'', RedirectView.as_view(url="home")),

]