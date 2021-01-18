"""mydjango URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
# urlpatterns = [
#     url(r'^$',views.hello),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),path('first/', views.first,name="firstpage"),url(r'^tags[\/]?', views.tags),url(r'^score[\/]?', views.score),url(r'^runoob[\/]?', views.runoob),url(r'^$',views.hello),url(r'\w+',views.erro)
]
