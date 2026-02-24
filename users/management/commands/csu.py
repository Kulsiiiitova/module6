from django.core.management.base import BaseCommand
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Add superuser to the database'

    def handle(self, *args, **options):
        user = CustomUser.objects.create(email="admin@mail.ru")
        user.set_password('admin')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()