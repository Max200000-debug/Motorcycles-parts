from .models import Item, Shipment, ItemShipmentGroup
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import PostForm


class IndexView(ListView):
    model = Item
    template_name = 'core/index.html'

class SingleView(DetailView):
    model = Item
    template_name = 'core/single.html'
    context_object_name = 'item'

class EditView(UpdateView):
    model = Item
    fields = '__all__'
    template_name = 'core/form.html'
    extra_context = {'submit_action': 'Edit'}
    def get_success_url(self, **kwargs):
        return reverse_lazy("core:save", args=(self.object.id,))

class AddView(CreateView):
    model = Item
    fields = '__all__'
    template_name = 'core/form.html'
    extra_context = {'submit_action': 'Add'}
    def get_success_url(self, **kwargs):
        return reverse_lazy("core:save", args=(self.object.id,))

class Delete(DeleteView):
    model = Item
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('core:index')
    template_name = 'core/confirm-delete.html'

def save(request, id):
    item = get_object_or_404(Item, pk=id)
    form = PostForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
    return redirect('core:index')

class CreateShipment(ListView):
    model = Item
    template_name = 'core/create-shipment.html'

def process_shipment(request):
    item_added = Item.objects.get(pk=request.POST['item'])
    shipment = Shipment.objects.create(
        name=request.POST['name'],
        description=request.POST['description'],
        date=request.POST['date'],
        status=request.POST['status'],
        )
    ItemShipmentGroup.objects.create(
        item=item_added,
        shipment=shipment,
        quantity=request.POST['quantity'],
        )
    messages.success(request, 'Shipment created successfully')
    return redirect('core:index')

class ViewShipmentSingle(DetailView):
    model = Shipment
    template_name = 'core/single-shipment.html'
    context_object_name = 'shipment'

class ViewShipments(ListView):
    model = Shipment
    template_name = 'core/shipments.html'