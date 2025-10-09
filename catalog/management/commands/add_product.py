from django.core.management.base import BaseCommand
from catalog .models import Category, Product


class Command(BaseCommand):
    help = 'Add product to the database'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category = Category.objects.create(category_name='детские товары', category_description='отдел с игрушками')

        products = [
            {'product_name': 'плюшевый мишка', 'product_description': '''Не просто игрушка, а самый верный друг!
            Этот плюшевый мишка с добрыми глазками-бусинками создан для того, чтобы дарить тепло и уют.''', 'product_category':category, 'price_product':'1000'},
            {'product_name': 'кукла', 'product_description': '''Искусство в деталях. Эта изысканная кукла ручной работы поражает своей утонченностью. 
            Роскошное платье из парчи и кружев.''', 'product_category': category, 'price_product': '1500'},
            {'product_name': 'плюшевый конь', 'product_description': '''Встречайте Рамиля — не обычную лошадку, а самого настоящего друга с гордым характером! 
            Этот статный конь с умными глазами и шелковистой гривой создан для тех, кто ценит верность и отвагу.''', 'product_category': category, 'price_product': '1500'},
            {'product_name': 'миньон', 'product_description': '''Банана! В вашем доме поселится самый обаятельный непоседа из всеми любимого мультфильма! 
            Миньон Боб повторяет забавные фразы и звуки, светится в темноте и обожает танцевать.''', 'product_category': category, 'price_product': '2000'},
            {'product_name': 'конструктор', 'product_description': '''Откройте безграничные возможности для творчества! 
            Этот конструктор — не просто набор деталей, а целая вселенная для развития инженерного мышления.''',
            'product_category': category, 'price_product': '3000'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exist: {product.product_name}'))