from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    # Aquí definimos las columnas que verás en la tabla principal
    list_display = ('nombre', 'email', 'telefono', 'interes', 'mensaje', 'created_at')
    
    # Esto agrega filtros laterales para encontrar leads más rápido
    list_filter = ('interes', 'created_at')
    
    # Esto permite buscar por nombre o email
    search_fields = ('nombre', 'email')
    
    # Esto define el orden en que ves los mensajes (del más nuevo al más antiguo)
    ordering = ('-created_at',)