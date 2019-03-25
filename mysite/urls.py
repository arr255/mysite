"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from first_app import views as first_app_views #new
from cal import views as cal_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',first_app_views.index),#new
    url(r'^manhua.html',first_app_views.manhua),
    url(r'^manhua/douluodalu.html',first_app_views.manhua_douluodalu),
    url(r'^face.html',first_app_views.face_recognition),
    url(r'^cal$',cal_views.inte),
    url(r'^calPage/$',cal_views.calHtml),
    url(r'^calPage/cal$',cal_views.cal),
    url(r'^calPage/myDiff',cal_views.myDiff),
]
