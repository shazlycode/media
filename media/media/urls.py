"""media URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('player/<int:channel_id>', views.ChannelPlayer, name='player'),
    path('radio', views.radio, name='radio'),
    path('rplayer/<int:radio_id>', views.RadioPlayer, name='radioplayer'),
    path('register', views.register,name='register'),
    path('login/', views.log, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('favorite_channel', views.favorite_channel, name='favorite_channel')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
