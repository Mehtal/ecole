from django.conf.urls import url
from django.views.generic.base import RedirectView
from grades import views

urlpatterns = [
    url(r'detail/(?P<pk>\d+)', views.GradeDetailView.as_view(), name='detail'),
    url(r'list/', views.PostListView.as_view(), name='list'),
]
