from django.urls import path
from django.http import HttpResponse



from . import views

urlpatterns = [
    path('cadastar_vendedor/', views.cadastar_vendedor, name="cadastar_vendedor")
]