from django.db import models


class SpecialLinks(models.Model):
    title = models.CharField('Título', max_length=30)
    url = models.URLField('Link')
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class SpecialCategory(SpecialLinks):
    """ """
    show_right = models.BooleanField(
        'Exibir junto com links importantes?',
        default=False
    )

    class Meta:
        verbose_name = 'Categoria especial'
        verbose_name_plural = 'Categorias especiais'

class ImportantLinks(SpecialLinks):
    """ """
    class Meta:
        verbose_name = 'Link importante'
        verbose_name_plural = 'Links importantes'
