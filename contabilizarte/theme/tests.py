from django.test import TestCase
from contabilizarte.theme.models import SpecialCategory, ImportantLinks


class SpecialCategoryTest(TestCase):
    def test_model(self):
        SpecialCategory.objects.create(
            title='Contabilidade na Prática',
            url='http://www.contabilizarte.com.br'
        )
        self.assertTrue(SpecialCategory.objects.exists())


class ImportantLinksTest(TestCase):
    def test_model(self):
        ImportantLinks.objects.create(
            title='Receita Federal',
            url='http://idg.receita.fazenda.gov.br/'
        )
        self.assertTrue(ImportantLinks.objects.exists())

