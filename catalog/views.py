from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'
    fields = ('name', 'phone', 'message')


    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")

            return HttpResponse(f'Спасибо {name}, сообщение получено!')
        return render(request, 'contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'price_product', 'product_category', 'product_picture', 'product_description')
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_list')
