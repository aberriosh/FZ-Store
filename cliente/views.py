from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Cuenta

# Create your views here.

class CuentaCreate(CreateView):
    model = Cuenta
    fields = '__all__'
    initial = {'cuent_fecnac':'01/01/2019',}
    success_url = reverse_lazy('paginas:inicio')

class CuentaUpdate(UpdateView):
    model = Cuenta
    fields = ['cuent_email','cuent_pass','cuent_nombre','cuent_desp','cuent_seg','cuent_pago']

class CuentaDelete(DeleteView):
    model = Cuenta
    success_url = reverse_lazy('Clientes')

from django.views import generic
class CuentaDetailView(generic.DetailView):
    model = Cuenta