from django import template
from django.db.models import Count
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.simple_tag
def get_most_сommented_posts(count=5):
    return (Post.publish.annotate(total_comments=Count('comments'))
            .order_by('-total_comments'))[:count]

@register.inclusion_tag('blogapp/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}
