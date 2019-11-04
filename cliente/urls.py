from django.urls import path
from . import views

app_name='cliente'

urlpatterns = [
    path('cuenta/create/',views.CuentaCreate.as_view(), name='reg'),
]