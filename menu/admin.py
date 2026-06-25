from django.contrib import admin
from .models import Pizza
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'prix', 'vegetarienne')
    search_fields = ('nom', 'ingredients')

admin.site.register(Pizza, PizzaAdmin)
