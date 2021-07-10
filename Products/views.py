from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from Products.models import Product
from Products.forms import ProductForm
from django.utils import timezone
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class ProductsListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')

class ProductsDetailView(DetailView):
    model = Product
    template_name='Products/products_detail.html'


class ProductsCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'Products/posts_detail.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')
    model = Product

class ProductsUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'Products/product_list.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('product_list')
    login_url = '/login/'

class ProductsDeleteView(LoginRequiredMixin,DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')
