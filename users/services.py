from django.core.cache import cache
from mymarket.models import Category

def get_cached_categories():
    categories = cache.get('categories')
    if not categories:
        categories = list(Category.objects.all())
        cache.set('categories', categories, timeout=60 * 30)  # Кеш на 30 минут
    return categories