"""Analytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_profile_func, name="home"),
    path('userUpdate/<int:id>', user_update_func, name="user_update_url"),
    path('userDelete/<int:id>', user_delete_func, name="user_delete_url"),
    path('firebase-messaging-sw.js',showFirebaseJS,name="show_firebase_js"),
    path('send/' , send),
]
