"""kportal URL Configuration

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
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

#from kapi.urls import router as kapi_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_jwt_token),
    #path('auth/', include('rest_framework.urls')),
    #path('auth/', include('social_django.urls', namespace='social')),
    #path('api/', include(kapi_router.urls)),
    path('member/', include('member.urls')),
    path('events/', include('events.urls')),
    path('concerts/', include('concerts.urls')),
]
