from django.conf.urls import url 
from blog.api.views import PostRudView,PostAPIView,PostLikeAPIToggle

urlpatterns = [
	url(r'detail/(?P<pk>\d+)/like/', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
    url(r'post/(?P<pk>\d+)', PostRudView.as_view(), name="api-rud"),
    url(r'list/', PostAPIView.as_view(), name="api-view"),
]