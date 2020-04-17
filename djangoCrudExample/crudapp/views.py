from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventory
from .forms import newInventoryForm
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = 'crudapp/index.html'
    context_object_name = 'inventory_list'

    def get_queryset(self):
        return Inventory.objects.all()

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'crudapp/inventory-detail.html'


def create(request):
    if request.method == 'POST':
        form = newInventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = newInventoryForm()

    return render(request,'crudapp/create.html',{'form': form})

def edit(request, pk, template_name='crudapp/edit.html'):
    contact = get_object_or_404(Inventory, pk=pk)
    form = newInventoryForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method=='POST':
        inventory.delete()
        return redirect('index')
    return render(request, template_name, {'object':inventory})