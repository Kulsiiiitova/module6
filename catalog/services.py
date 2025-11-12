from .models import Product, Category


class ProductService:
    @staticmethod
    def get_products(category_name):
        category = Category.objects.get(category_name=category_name)
        products = Product.objects.filter(
            product_category=category,
            is_published=True
        )
        return products
