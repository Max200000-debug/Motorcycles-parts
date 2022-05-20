from email.mime import image
from unicodedata import category
from django.db import models
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    description = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    
    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.name


class Shipment(models.Model):
    items = models.ManyToManyField(Item, through='ItemShipmentGroup')
    published = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return str(self.id)


class ItemShipmentGroup(models.Model):
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()