from django.contrib import admin

from .models import FotoUrl, Media, Prueba, Torneo

# Register your models here.
admin.site.register(Prueba)
admin.site.register(Media)
admin.site.register(Torneo)
admin.site.register(FotoUrl)