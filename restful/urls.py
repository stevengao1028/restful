"""restful URL Configuration

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
from django.conf.urls import url, include
from apitest.models import  *
from rest_framework import routers, serializers, viewsets
from apitest.serializer import *
from apitest import views
from rest_framework.urlpatterns import format_suffix_patterns


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^api', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home,name='home'),
    url(r'^profit_list/$', views.profit_list,name='profit_list'),
    #url(r'^person_list/$', views.person_list, name='person_list'),
    #url(r'^profit_list/(?P<code>\d+)/$', views.profit_list,name='profit_list'),
]
# urlpatterns = format_suffix_patterns(urlpatterns)