from django.urls import path
from catalog.apps import CatalogConfig
from catalog import views
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ContactsTemplateView, \
    ProductDeleteView, ProductUpdateView, CanUnpublishProduct, category_products

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_form/', ProductCreateView.as_view(), name='product_form'),
    path('product_details/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/unpublish_product/', CanUnpublishProduct.as_view(), name='unpublish_product'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),
    path('category/<str:category_name>/', views.category_products, name='category_products'),
]