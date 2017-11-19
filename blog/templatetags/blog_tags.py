from django import template
from ..models import Post, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.assignment_tag
def get_recent_posts(num=5):
	return Post.objects.all().order_by('-read_amount')[:num]

@register.assignment_tag
def archives():
    return Post.objects.datetimes('create_time', 'month', order='DESC')
	
	
@register.assignment_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    #return Category.objects.all()
	return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.assignment_tag	
def get_tag():
	return Tag.objects.annotate(num_posts=Count('post'))