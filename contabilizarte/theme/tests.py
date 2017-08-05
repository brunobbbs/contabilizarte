from django.test import TestCase
from contabilizarte.theme.models import SpecialCategory, ImportantLinks


class SpecialCategoryTest(TestCase):
    def test_model(self):
        SpecialCategory.objects.create(
            title='Contabilidade na Prática',
            url='http://www.contabilizarte.com.br',
            active=True,
        )
        self.assertTrue(SpecialCategory.objects.exists())


class ImportantLinksTest(TestCase):
    def setUp(self):
        ImportantLinks.objects.create(
            title='GitHub do Bruno',
            url='https://github.com/brunobbbs',
            active=True,
        )

    def test_model(self):
        self.assertTrue(ImportantLinks.objects.exists())

    def test_important_links_display_on_home_if_active(self):
        resp = self.client.get('/')
        self.assertContains(
            resp,
            '<a href="https://github.com/brunobbbs"',
        )

