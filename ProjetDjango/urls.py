"""ProjetDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import  ChDroitErreur, ChiffrementGauche, DchDroitErreur, DchGaucheErreur, DechiffrementDroit, DechiffrementGauche, Index ,ChiffrementDroit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='HomePage'),
    path('ChiffreDroit',ChiffrementDroit,name='ChiffreDroit'),
    path('ChiffreGauche',ChiffrementGauche,name='ChiffreGauche'),
    path('DechiffreDroit',DechiffrementDroit,name='DechiffreDroit'),
    path('DechiffreGauche',DechiffrementGauche,name='DechiffreGauche'), 
    path('ChD',ChDroitErreur,name='ChD'),
    path('ChG',ChDroitErreur,name='ChG'),
    path('DchD',DchDroitErreur,name='DchD'),
    path('DchG',DchGaucheErreur,name='DchG'),
]
