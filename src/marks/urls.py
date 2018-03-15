from django.conf.urls import url
from marks import views


urlpatterns = [
	
	url(r'update/(?P<pk>[\w.@+-]+)/', views.MarksUpdateView.as_view(), name='marks-update'),
	url(r'list/', views.MarksListView.as_view(), name='marks-list'),
	url(r'create/', views.MarksCreateView.as_view(), name='marks-create'),
	url(r'ajax/' , views.load_teachers , name="load_teachers" )
]
    
