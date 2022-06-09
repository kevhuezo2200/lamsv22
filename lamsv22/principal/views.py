from django.shortcuts import render, HttpResponse
from .models import Project



# Create your views here.
def home(request):
    return render(request,"principal/home.html")

def about(request):
   return render(request,"principal/about.html")


def contact(request):
    return render(request,"principal/contacto.html")

def about(request):
   return render(request,"principal/prueba.html")

# modificacion para pantalla admin 

def portfolio(request):
    projects = Project.objects.all()
    return render(request, "principal/portafolio.html", {'projects':projects})