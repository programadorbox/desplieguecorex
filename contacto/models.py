from django.db import models

class Lead(models.Model):
    TOPICS = [
        ('trazabilidad', 'Trazabilidad'),
        ('canchas', 'Arriendo de canchas'),
        ('escuelas', 'Escuelas de fútbol'),
        ('farmacia', 'Farmacia / retail'),
        ('otro', 'Otro'),
    ]
    nombre = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=40, blank=True)
    interes = models.CharField(max_length=30, choices=TOPICS, default='otro')
    mensaje = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} — {self.interes}"
