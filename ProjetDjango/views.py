from email import message
import imp
from django.forms import NullBooleanField
from django.http import HttpResponse
from django.shortcuts import render
from .chiffrement import chiffrement
from .dechiffrement import dechiffrement
from .exo import Calcule


def Index(request):
    valeur = ''
    if request.method == "POST":
         valeur = int(request.POST.get("val"))
    return render(request,"index.html",context={"val":Calcule(valeur)})


def ChiffrementDroit(request):
    message = ''
    maclee = ''
    result = ''
    if request.method == "POST":
      if  len(request.POST.get("Clee")) == 0:
          return render(request,'ChDroitErreur.html')    
      elif len(request.POST.get("Clee")) == 0:
          return render(request,'ChDroitErreur.html')
      maclee = int(request.POST.get("Clee"))
      if  maclee < 0 :
          return render(request,'ChDroitErreur.html')
      message = request.POST.get("message")
      maclee = maclee%26  
      result  = chiffrement(message,maclee)
    return render(request,"ChiffrementDroit.html",context={'K':result})   


def ChiffrementGauche(request):
    message = ''
    maclee = ''
    resultat = ''
    if request.method == "POST":
      if  len(request.POST.get("Clee")) == 0:
          return render(request,'ChGaucheErreur.html')    
      elif len(request.POST.get("Clee")) == 0:
          return render(request,'ChGaucheErreur.html')
      maclee = int(request.POST.get("Clee"))
      if  maclee < 0 :
          return render(request,'ChGaucheErreur.html') 
      maclee = maclee%26
      message = request.POST.get("message")
      resultat  = dechiffrement(message,maclee)
    return render(request,"ChiffrementGauche.html",context={'K2':resultat})

def DechiffrementDroit(request):
    message = ''
    maclee = ''
    result = ''
    if request.method == "POST":
      if  len(request.POST.get("Clee")) == 0:
          return render(request,'DchDroitErreur.html')    
      elif len(request.POST.get("Clee")) == 0:
          return render(request,'DchDroitErreur.html')
      maclee = int(request.POST.get("Clee"))
      if  maclee < 0 :
          return render(request,'DchDroitErreur.html')
      message = request.POST.get("message")
      maclee = maclee%26  
      result  = chiffrement(message,maclee)
    return render(request,"DechiffrementGauche.html",context={'decipher2':result}) 


def DechiffrementGauche(request):
    message = ''
    maclee = ''
    resultat = ''
    if request.method == "POST":
      if  len(request.POST.get("Clee")) == 0:
          return render(request,'DchGaucheErreur.html')    
      elif len(request.POST.get("Clee")) == 0:
          return render(request,'DchGaucheErreur.html')
      maclee = int(request.POST.get("Clee"))
      if  maclee < 0 :
          return render(request,'DchGaucheErreur.html')
      maclee = maclee%26
      message = request.POST.get("message")
      resultat  = dechiffrement(message,maclee)
    return render(request,"DechiffrementDroit.html",context={'decipher':resultat})


def ChDroitErreur(request):
    return 0   

def ChGaucheErreur(request):
    return 0    

def DchDroitErreur(request):
    return 0   

def DchGaucheErreur(request):
    return 0 