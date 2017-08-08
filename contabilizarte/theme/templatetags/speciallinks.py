from django import template
from contabilizarte.theme.models import SpecialCategory, ImportantLinks

register = template.Library()


CATEGORIES_COLOR_ORDERING = ['laranja', 'azul', 'verde', 'amarelo']


@register.simple_tag
def render_important_links():
    return ImportantLinks.objects.filter(active=True)


@register.simple_tag
def render_special_categories():
    categories = SpecialCategory.objects.filter(active=True)
    colors = get_category_colors(categories.count())
    return zip(categories, colors)


def get_category_colors(max_value=1):
    import itertools
    qtd = 0
    for color in itertools.cycle(CATEGORIES_COLOR_ORDERING):
        if qtd >= int(max_value):
            break
        qtd += 1
        yield color
