from django.urls import path
from .views import VRegistro, cerrar_sesion, logear

urlpatterns = [
    path('', VRegistro.as_view(), name="sign_up"),
    path('login/', logear, name="login"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion")
]
