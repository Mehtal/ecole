"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from accounts  import views as accounts_views
from blog.views import PostListView

urlpatterns = [
    # url(r'^', include('events.urls', namespace='events')),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/student$', accounts_views.StudentSignUpView.as_view(), name='student_signup'),
    url(r'^signup/teacher$', accounts_views.TeacherSignUpView.as_view(), name='teacher_signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'blog/', include('blog.urls', namespace='blog')),
    url(r'marks/', include('marks.urls', namespace='marks')),
    url(r'api/blog/', include('blog.api.urls', namespace='api_blog')),
    url(r'^$',  accounts_views.HomeListView.as_view(), name='home'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

