from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactsTemplateView, \
    ProductDeleteView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
    path('product_details/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit')
]