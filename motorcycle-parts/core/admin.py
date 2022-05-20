from django.contrib import admin
from .models import Item, Shipment, ItemShipmentGroup

admin.site.register(Item)
admin.site.register(Shipment)
admin.site.register(ItemShipmentGroup)