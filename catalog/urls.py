from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
    path('product_details/<int:pk>/', ProductDetailView.as_view(), name='product_details')
]