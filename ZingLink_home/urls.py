"""
URL configuration for ZingLink_home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index, name='index'),
    path('messages/',Messages, name='messages'),
    path('friends/',Friends, name='friends'),
    path('user-settings/',Settings_page, name='settings'),
    path('login-user/',Login_page, name='login_page'),
    path('register-user/',Register_page, name='register_page'),
    path('logout-user/',Logout_page, name='logout-user'),
    path('profile-update/',profile_view, name='profile-update'),
    path('add-news/',Add_news, name='add-news'),
    path('add-post/',Add_post, name='add-post'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()