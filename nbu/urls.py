"""nbu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views
import settings

urlpatterns = [
    url(r'^$',learn_views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^insert/',learn_views.insert),
    url(r'^show/',learn_views.list),
    url(r'^home/',learn_views.job),
    url(r'^policy_json/',learn_views.policy_json),
    url(r'^policy/',learn_views.policy_html),
]
