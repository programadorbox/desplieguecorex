import logging
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Lead

# Configura un logger para capturar errores
logger = logging.getLogger(__name__)

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(f"DATOS RECIBIDOS: {request.POST}")
        try:
            # Aquí capturamos los datos
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            
            # Intento de guardado
            Lead.objects.create(
                nombre=nombre, 
                email=email,
                empresa=request.POST.get('empresa'),
                telefono=request.POST.get('telefono'),
                interes=request.POST.get('interes', 'otro'),
                mensaje=request.POST.get('mensaje')
            )
            return render(request, 'contacto/index.html', {'message': 'Éxito'})
            
        except Exception as e:
            # ESTO ES LO IMPORTANTE:
            # Obliga a Django a escribir el error detallado en los logs de Render
            logger.exception("ERROR CRÍTICO AL GUARDAR EL LEAD")
            # Devolvemos un 500 para el usuario, pero el detalle está en los logs
            return render(request, 'contacto/index.html', {'message': 'Error interno'})
            
    return render(request, 'contacto/index.html')