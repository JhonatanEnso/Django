from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'informacion/index.html')
    #return HttpResponse("Mi primera pagina Django!!!")

def pelis(request):
    return render(request, 'informacion/pelis.html')

def futbol(request):
    nombre = "Lionel Messi"
    data = {
        "equipo": nombre
    }
    return render(request, 'informacion/futbol.html', data)

def jugadores(request):
    return render(request, 'informacion/jugadores.html') 
    #return HttpResponse("Mi primera pagina Django!!!")