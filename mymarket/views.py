from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse
from django.utils.text import slugify
from .models import BlogPost

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def index(request):
    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'index.html', context)


class ContactView(TemplateView):
    template_name = 'contacts.html'

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'
    queryset = BlogPost.objects.filter(is_published=True)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_count += 1
        obj.save()
        return obj

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        new_blog = form.save(commit=False)
        new_blog.slug = slugify(new_blog.title)
        new_blog.save()
        return super().form_valid(form)

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('blogpost_detail', args=(self.object.pk,))

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogpost_confirm_delete.html'
