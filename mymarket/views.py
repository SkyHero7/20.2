from django.shortcuts import render
from .models import Product

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def index(request):
    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'index.html', context)