from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza

# Create your views here.
def index(request):
    """
    pizzas = Pizza.objects.all()
    pizzas_names = [pizza.nom for pizza in pizzas]
    pizzas_names = ', '.join(pizzas_names)
    """
    pizzas = Pizza.objects.all()
    return render(request, 'menu/index.html', {'pizzas': pizzas})