from django.conf.urls import url
from events import views


urlpatterns = [
	url(r'', views.EventCreate.as_view() ,name='teacher'),
]
    
