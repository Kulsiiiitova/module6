from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import View
from django.contrib import messages
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .services import ProductService
from .forms import ProductForm

from .models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        cache_key = 'published_products'
        queryset = cache.get('catalog_queryset')

        if not queryset:
            queryset = Product.objects.filter(is_published=True)
            cache.set(cache_key, queryset, 60 * 15)  # Кешируем на 15 минут
        return queryset


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


@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_details.html'
    context_object_name = 'product'


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')
    context_object_name = 'product'
    permission_required = 'products.can_delete_product'

    def test_func(self):
        product = self.get_object()
        is_owner = self.request.user == product.author
        is_moderator = self.request.user.has_perm('catalog.can_delete_product')
        return is_owner or is_moderator

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав для удаления продуктов')
        return redirect('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        prod = get_object_or_404(Product, pk=self.kwargs["pk"])
        return self.request.user == prod.author


class CanUnpublishProduct(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации.")

        if product.is_published:
            product.is_published = False
            product.save()

        return redirect('catalog:product_list')


def category_products(request, category_name):
    products = ProductService.get_products(category_name)
    category = get_object_or_404(Category, category_name=category_name)

    context = {
        'products': products,
        'category': category,
    }

    return render(request, 'products_category.html', context)

