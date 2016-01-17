"""cookdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings #needed to check for debug status etc..

from rest_framework.urlpatterns import format_suffix_patterns
from users import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^usertest/(?P<userid>\d+)$', views.user_test, name='user_test'),
    url(r'^api-auth/$', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/$', views.UserList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

