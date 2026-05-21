from django.shortcuts import render
from django.http import HttpResponse # <--- ESTO ES LO NUEVO
from .models import Lead
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    # Esto es lo que reemplaza a tu función actual
    if request.method == 'POST':
        try:
            # Aquí va toda tu lógica de captura de datos
            nombre = request.POST.get('nombre', '')
            # ... resto de tus campos ...
            
            # Aquí va tu lógica de guardado
            Lead.objects.create(nombre=nombre, ...) 
            
            return render(request, 'contacto/index.html', {'message': 'Éxito'})
        except Exception as e:
            # Esto es el "debug": si algo falla, no da error 500, 
            # muestra el error real en pantalla
            return HttpResponse(f"Error detectado: {str(e)}", status=500)
    
    return render(request, 'contacto/index.html')