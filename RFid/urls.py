"""RFid URL Configuration

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
from rfidApp.views import *

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'dashboard/users/(?P<id>[0-9]+)/$', presence, name='presence'),
    url(r'dashboard/users/sup/(?P<id>[0-9]+)/$', sup, name='sup'),
    url(r'dashboard/add', adduser, name='adduser'),
    url(r'store/', test, name='test'),

    url(r'dashboard/', users, name='users'),
    url(r'logout/', logout, name='logout'),

    url(r'', home,name='home'),

]
