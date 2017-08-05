from django import template
from contabilizarte.theme.models import SpecialCategory, ImportantLinks

register = template.Library()


@register.simple_tag
def special_links(_type='important-links'):
    if _type == 'category':
        links = SpecialCategory.objects.filter(active=True)
    else:
        links = ImportantLinks.objects.filter(active=True)
    return links
