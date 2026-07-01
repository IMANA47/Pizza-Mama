
from django.urls import path
from . import views
app_name = 'menu'
urlpatterns = [
    path('api/pizzas/', views.api_get_pizzas, name='api_get_pizzas'),
]
