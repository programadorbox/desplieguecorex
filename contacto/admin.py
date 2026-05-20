from django.contrib import admin
from .models import Lead
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'interes', 'created_at')
    list_filter = ('interes',)
