from django.shortcuts import render
from .models import Lead
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    message = None
    if request.method == 'POST':
        # Captura de datos
        nombre = request.POST.get('nombre', '').strip()
        empresa = request.POST.get('empresa', '').strip()
        email = request.POST.get('email', '').strip()
        telefono = request.POST.get('telefono', '').strip()
        interes = request.POST.get('interes', 'otro').strip()
        mensaje = request.POST.get('mensaje', '').strip()

        if nombre and email:
            # Persistencia en MySQL (Aiven)
            Lead.objects.create(
                nombre=nombre, empresa=empresa, email=email,
                telefono=telefono, interes=interes, mensaje=mensaje
            )
            message = 'Gracias — tus datos fueron registrados correctamente.'
        else:
            message = 'Por favor completa los campos Nombre y Email.'

    return render(request, 'contacto/index.html', {'message': message})