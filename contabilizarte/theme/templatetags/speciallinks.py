from django import template
from itertools import chain
from contabilizarte.theme.models import SpecialCategory, ImportantLinks

register = template.Library()


CATEGORIES_COLOR_ORDERING = ['laranja', 'azul', 'verde', 'amarelo']


@register.simple_tag
def render_important_links():
    importantlinks = ImportantLinks.objects.filter(active=True)
    specialcategories = SpecialCategory.objects.filter(
        show_right=True, active=True
    )
    return list(chain(importantlinks, specialcategories))


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
