from django.contrib import admin
from .models import Cliente, Habitacion

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'correo','fecha_ingreso')
    list_filter = ('fecha_ingreso',)
    search_fields = ('nombre', 'apellido', 'correo')
    ordering = ('-fecha_ingreso',)

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero_habitacion', 'tipo_habitacion', 'precio_por_noche', 'disponible')
    list_filter = ('tipo_habitacion', 'disponible')
    search_fields = ('numero_habitacion',)
    ordering = ('numero_habitacion',)




# Register your models here.
