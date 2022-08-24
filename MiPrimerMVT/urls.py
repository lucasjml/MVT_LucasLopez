from django.contrib import admin
from django.urls import path
from AppFamilia.views import mostrar_familia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', mostrar_familia ),
]
