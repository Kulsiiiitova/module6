from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product
from django.contrib.contenttypes.models import ContentType
from django.apps import apps

class Command(BaseCommand):
    help = 'Add groups to the database'

    def handle(self, *args, **options):
        groups = ['Product moderator']

        for group_name in groups:
            Group.objects.filter(name=group_name).delete()

        content_type = ContentType.objects.get_for_model(Product)

        unpublish_permission = Permission.objects.get(
            codename='can_unpublish_product',
            content_type=content_type
        )

        delete_permission = Permission.objects.get(
            codename='delete_product',
            content_type=content_type
        )
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            # Добавляем разрешения к группе
            group.permissions.add(unpublish_permission, delete_permission)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added group: {group}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exist: {group}'))
