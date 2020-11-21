"""testSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import os
from django.contrib import admin
from django.urls import path,include,re_path

# from django.conf.urls import url  #depricated(alias used: re_path())
from django.views.static import serve

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('\n',BASE_DIR)
SITE_ROOT = os.path.join(BASE_DIR,'site')
CSS_ROOT = os.path.join(BASE_DIR,'css')
urlpatterns = [
    path('',include('home.urls',namespace='home')),
    path('admin/', admin.site.urls),
    path('polls/',include('polls.urls')),
    re_path(r'^site/(?P<path>.*)$',serve,
        {'document_root' : SITE_ROOT,'show_indexes': True},
        name='site_path'
    ),
    re_path(r'^css/(?P<path>.*)$',serve,
        {'document_root':CSS_ROOT,'show_indexes':True},
        name='css_test'
    ),
    path('samples/',include('samples.urls',namespace='samples')),
    path('music/',include('MusicLib.urls',namespace='music')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('authz/',include('authz_dj4e.urls')),
    path('autos/',include('autos_dj4e.urls',namespace='autos')),
    path('crispy/',include('crispy_dj4e.urls',namespace='crispy')),
    # path('unesco/',include('unesco.urls',namespace='unesco')),
    path('bootstrap/',include('bootstrap_learn.urls',namespace='bs4')),
]

