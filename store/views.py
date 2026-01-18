from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from store.models import Product
from .forms import ProductModelForm

def index(request):
    """Главная страница."""
    context = {
        'title': 'Главная страница !'
    }
    return render(request, 'base.html', context=context)

def about_view(request):
    """О нас"""
    return render(request, 'store/about.html')

def product_list(request):
    """Список товаров"""
    products = Product.objects.all()
    context = {
        'title': 'Список товаров',
        'products': products,
    }
    return render(request, 'store/product_list.html', context)

def product_detail(request, product_id):
    """Детальная инфа о товаре"""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'title': product.name,
        'product': product,
    }
    return render(request, 'store/product_detail.html', context)

def product_add(request):
    """Добавление нового товара"""
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductModelForm()
    
    context = {
        'title': 'Добавить новый товар',
        'form': form,
    }
    return render(request, 'store/product_form.html', context)


def product_edit(request, product_id):
    """Редактирование товара"""
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = ProductModelForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductModelForm(instance=product)
    
    context = {
        'title': f'Редактировать {product.name}',
        'form': form,
        'product': product,
    }
    return render(request, 'store/product_form.html', context)