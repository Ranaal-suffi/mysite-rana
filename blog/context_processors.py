"""missing"""
from django.db.models import Count
from . import models

def base_context(request):
    """missing"""
    authors = models.Post.objects.published() \
        .get_authors() \
        .order_by('first_name')
    topics = models.Topic.objects.all().annotate(num_posts= Count('blog_posts'))\
        .order_by('-num_posts')

    return {'authors': authors, 'topics': topics}
def get_topics(request):
    """missing"""
    return models.Topic.objects.all().annotate(num_posts=Count('blog_posts'))\
        .order_by('-num_posts')
