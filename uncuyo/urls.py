from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.index, name="index"),
    path("disciplinas", views.sumate, name="sumate"),
    path("disciplinas/<str:prueba>", views.prueba, name="prueba"),
    path("planes-de-entrenamiento", views.planes, name="planes"),
    path("fotos", views.fotos, name="fotos")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()