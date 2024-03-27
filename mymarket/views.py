from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Product, Version
from .forms import ProductForm, VersionForm
from django.views.generic import ListView
from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    form = ProductForm()
    return render(request, 'product_form.html', {'form': form, 'form_show_errors': True})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})
class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'version_create.html'
    success_url = reverse_lazy('version_list')

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    template_name = 'version_update.html'
    success_url = reverse_lazy('version_list')

class VersionDeleteView(DeleteView):
    model = Version
    template_name = 'version_confirm_delete.html'
    success_url = reverse_lazy('version_list')

class VersionListView(ListView):
    model = Version
    template_name = 'version_list.html'

class VersionDetailView(DetailView):
    model = Version
    template_name = 'version_detail.html'