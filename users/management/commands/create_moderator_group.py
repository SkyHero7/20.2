from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Creates a moderator group and assigns permissions for product management'

    def handle(self, *args, **options):
        from mymarket.models import Product  # Отложенный импорт модели Product

        # Создание группы модераторов
        moderator_group, created = Group.objects.get_or_create(name='Moderators')

        # Получение разрешений для управления продуктами
        product_content_type = ContentType.objects.get_for_model(Product)
        can_change_product = Permission.objects.get(content_type=product_content_type, codename='change_product')
        can_cancel_product = Permission.objects.get(content_type=product_content_type, codename='cancel_product')
        can_change_description = Permission.objects.get(content_type=product_content_type, codename='change_description')

        # Назначение разрешений группе модераторов
        moderator_group.permissions.add(can_change_product, can_cancel_product, can_change_description)

        self.stdout.write(self.style.SUCCESS('Moderator group created and permissions assigned successfully.'))
