from django.shortcuts import render
from django.db import connection
from .models import Cliente, Habitacion
from django.shortcuts import render



def home(request): 
    return render(request, 'home.html')

def habitacion_disponible_base_datos(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM hotel_habitacion WHERE disponible = True")
        rows = cursor.fetchall()
        
    return render(request, 'habitaciones_db.html', {'habitaciones': rows})

def lista_clientes_base_datos(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM hotel_cliente ORDER BY fecha_ingreso DESC")
        rows = cursor.fetchall()

    return render(request, 'clientes_db.html', {'clientes': rows})


def habitacion_disponible(request):
    habitaciones = Habitacion.objects.filter(disponible=True)
    return render(request, 'habitaciones.html', {'habitaciones': habitaciones})

# Create your views here.
def lista_clientes(request):
    clientes = Cliente.objects.raw('SELECT * FROM hotel_cliente ORDER BY fecha_ingreso DESC')
    return render(request, 'clientes.html', {'clientes': clientes})


