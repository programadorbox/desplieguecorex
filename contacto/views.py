from django.shortcuts import render
from django.db import DatabaseError
from .models import Lead
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    message = None
    if request.method == 'POST':
        # Captura de datos con validación básica
        nombre = request.POST.get('nombre', '').strip()
        email = request.POST.get('email', '').strip()
        empresa = request.POST.get('empresa', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        interes = request.POST.get('interes', 'otro').strip()
        mensaje = request.POST.get('mensaje', '').strip()

        if nombre and email:
            try:
                # Persistencia en MySQL (Aiven)
                Lead.objects.create(
                    nombre=nombre, 
                    empresa=empresa, 
                    email=email,
                    telefono=telefono, 
                    interes=interes, 
                    mensaje=mensaje
                )
                message = 'Gracias — tus datos fueron registrados correctamente.'
            except DatabaseError:
                # Esto atrapa errores de conexión a Aiven o tablas faltantes
                message = 'Ocurrió un error al guardar en la base de datos. Inténtalo más tarde.'
        else:
            message = 'Por favor completa los campos obligatorios: Nombre y Email.'

    return render(request, 'contacto/index.html', {'message': message})