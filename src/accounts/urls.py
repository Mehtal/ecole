from django.conf.urls import url
from accounts import views


urlpatterns = [
	url(r'profile/(?P<username>[\w.@+-]+)/', views.ProfileDetailView.as_view(), name='profile'),
	url(r'update/(?P<username>[\w.@+-]+)/', views.edit_profile, name='update'),
	url(r'grade/(?P<name>[\w.@+-]+)/', views.GradeDetailView.as_view(), name='grade'),
]
    
