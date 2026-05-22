from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    # Usamos display_interes para ver el texto legible (ej: "Trazabilidad")
    list_display = ('nombre', 'email', 'telefono', 'display_interes', 'mensaje', 'created_at')
    
    # Filtros laterales
    list_filter = ('interes', 'created_at')
    
    # Buscador
    search_fields = ('nombre', 'email')
    
    # Orden cronológico (más nuevo primero)
    ordering = ('-created_at',)

    # Función para convertir el valor interno (ej: 'trazabilidad') en texto legible (ej: 'Trazabilidad')
    def display_interes(self, obj):
        return obj.get_interes_display()
    
    display_interes.short_description = 'Interés'