from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Cat
from .forms import CatForm

def about(request):
    return render(request, 'cats/about.html')
def cat_list(request):
    query = request.GET.get('q')
    order_by = request.GET.get('order_by', 'name')
    if query:
        cats = Cat.objects.filter(Q(name__icontains=query) | Q(breed__icontains=query)).order_by(order_by)
    else:
        cats = Cat.objects.all().order_by(order_by)
    return render(request, 'cats/cat_list.html', {'cats': cats, 'query': query, 'order_by': order_by})

def cat_create(request):
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm()
    return render(request, 'cats/cat_form.html', {'form': form})

def cat_update(request, pk):
    cat = Cat.objects.get(pk=pk)
    if request.method == 'POST':
        form = CatForm(request.POST, instance=cat)
        if form.is_valid():
            form.save()
            return redirect('cat_list')
    else:
        form = CatForm(instance=cat)
    return render(request, 'cats/cat_form.html', {'form': form})

def cat_delete(request, pk):
    cat = Cat.objects.get(pk=pk)
    cat.delete()
    return redirect('cat_list')
