from django.shortcuts import render
from .models import *

# Create your views here.
def navigation(request):
    return render(request, "navigation.html")


def footer(request):
    return render(request, "footer.html")

def home(request):
    Narsa = Product.objects.all()
    return render(request, "home.html", {"items" : Narsa})


def topshirish_punkiti(request):
    return render(request, "topshirish_punkiti.html")

def detail(request, id):
    mahsulot = Product.objects.get(id=id)
    context = {
        "mahsulot": mahsulot  
    }
    return render(request, "detail.html", context)
def sotuvchi_bolish(request):
    return render(request, "sotuvchi_bolish.html")

def sotuv(request):
    return render(request, "sotuv.html")
def savol(request):
    return render(request, "savol.html")
def sotuvchilik(request):
    return render(request, "sotuvchilik.html")
def splash(request):
    return render(request, 'splash.html')
