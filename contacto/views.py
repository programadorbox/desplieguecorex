from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
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
            # Persistencia en MySQL
            lead = Lead.objects.create(
                nombre=nombre, empresa=empresa, email=email,
                telefono=telefono, interes=interes, mensaje=mensaje
            )
            # Envío de email
            subject = f"Nuevo lead CorexAndes: {lead.nombre} — {lead.interes}"
            body = f"Nombre: {lead.nombre}\nEmpresa: {lead.empresa}\nEmail: {lead.email}\nTelefono: {lead.telefono}\nInteres: {lead.interes}\nMensaje:\n{lead.mensaje}"
            
            try:
                send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER], fail_silently=False)
                message = 'Gracias — tu mensaje fue enviado correctamente.'
            except Exception as e:
                message = 'Gracias — guardamos tu contacto, pero falló el envío del email.'
        else:
            message = 'Por favor completa los campos Nombre y Email.'

    return render(request, 'contacto/index.html', {'message': message})