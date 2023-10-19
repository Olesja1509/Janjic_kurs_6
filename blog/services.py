from django.conf import settings
from django.core.cache import cache

from blog.models import Article


def get_blog_cache():
    if settings.CACHE_ENABLED:
        key = 'article_detail'
        article_detail = cache.get(key)
        if article_detail is None:
            article_detail = Article.objects.all()
            cache.set(key, article_detail)
    else:
        article_detail = Article.objects.all()

    return article_detail
