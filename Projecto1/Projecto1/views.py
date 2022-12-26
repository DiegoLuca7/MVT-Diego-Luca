from django.http import HttpResponse
from datetime import datetime 
from django.shortcuts import render

def hello_world(request):
    return HttpResponse("Hola mundo")

def bye_world(request):
    return HttpResponse("chau")

def fecha_actual(request):
    hoy = datetime.now().date()
    return HttpResponse(f"La fecha de hoy es {hoy}")  

def vista_con_template(request):
    return render(request, "template.html" , context={})

def familia_template(request):
    nombre = "Monica"
    apellido = "Francia"
    edad = "49"
    nomb1 = "Noelia"
    nomb2 = "Morena"
    ap1 = "Luca"
    ap2 = "Miceli"
    edad1 = "29"
    edad2 = "13"
    context = {
        "nombre" : nombre,
        "apellido" : apellido,
        "edad" : edad,
        "nomb1" : nomb1,
        "nomb2" : nomb2,
        "ap1" : ap1,
        "ap2" : ap2,
        "edad1" : edad1,
        "edad2" : edad2,
    }
    return render(request, "familia.html" , context= context)

def regalos_template(request):
    context = {
        "regalos" : ["Pelota", "Videojuego", "Muñeca", "Bicicleta"],
    }
    return render(request, "regalos_navidad.html" , context= context)
