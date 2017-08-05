from django.db import models


class SpecialLinks(models.Model):
    title = models.CharField('Título', max_length=30)
    url = models.URLField('Link')
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class SpecialCategory(SpecialLinks):
    """ """

class ImportantLinks(SpecialLinks):
    """ """
