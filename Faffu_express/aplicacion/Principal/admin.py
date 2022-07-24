from django.contrib import admin
from .models import Cliente, pedido, aperitivos, pedido_aperitivo, bebidas, bebidas_pedido, facturas

# Register your models here.

admin.site.register(Cliente)
admin.site.register(pedido)
admin.site.register(aperitivos)
admin.site.register(pedido_aperitivo)
admin.site.register(bebidas)
admin.site.register(bebidas_pedido)
admin.site.register(facturas)