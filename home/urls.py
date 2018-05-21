"""hzbooks URL Configuration

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
from django.conf.urls import url,include
from django.conf.urls import url,include,patterns
from django.contrib import admin

import views
from rest_framework import routers

from rest_framework import routers
from .views import BookViewSet

# router = routers.DefaultRouter()
# router.register(r'students', BookViewSet)
#
# urlpatterns = [
#     url(r'^docs/', include('rest_framework_swagger.urls')),
# ]
# urlpatterns += router.urls
urlpatterns =  patterns('home.views',
    url(r'^$', views.index),
    url(r'^bookcreate/$', views.BookBaseCreate.as_view(), name='bookcreate'),
    url(r'^booklist/$', views.BookBaseList.as_view(), name='booklist'),
    url(r'^bookdetail/(?P<pk>[0-9]+)/$', views.BookBaseDetail, name='book_detail'),
    url(r'^bookdetail/(?P<pk>[0-9]+)/$', views.BookBaseDetail.as_view(), name='book_detail'),
    url(r'^docs/', include('rest_framework_swagger.urls'))
                        )

