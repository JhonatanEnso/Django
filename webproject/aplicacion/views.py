from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'aplicacion/index.html')
    #return HttpResponse("Mi primera Pagina Web con Django!!")

def metodoviernes(request):
    
    return render(request, 'aplicacion/viernes.html')
    #return HttpResponse("Hoy es viernes!!")

def metodolistas(request):
    return render(request, 'aplicacion/listas.html')

def metodopeliculas(request):
    return render(request, 'aplicacion/peliculas.html')
    #return HttpResponse("Listas en Django!!")
