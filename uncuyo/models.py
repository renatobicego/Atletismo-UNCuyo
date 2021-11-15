from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Prueba(models.Model):
    abr = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    descripción = models.TextField()
    pista = models.BooleanField()
    record = models.CharField(max_length=30, blank=True)
    frecord = models.CharField(max_length=30, blank=True)
    atleta = models.CharField(max_length=60, blank=True)
    atletaf = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return f"{self.nombre}"

class Media(models.Model):
    prueba_id = models.ForeignKey(Prueba, on_delete=CASCADE)
    image = models.ImageField(blank=True)
    def __str__(self):
        return f"{self.prueba_id.abr}"

class Torneo(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateField(default=None)
    image_cover = models.ImageField()
    class Meta:
        ordering = ['-fecha']
    def __str__(self):
        return f"{self.nombre}"

class FotoUrl(models.Model):
    torneo_id = models.ForeignKey(Torneo, on_delete=CASCADE)
    nombre = models.CharField(max_length=30)
    url = models.CharField(max_length=300)
    def __str__(self):
        return f"{self.torneo_id.nombre}, {self.nombre}"