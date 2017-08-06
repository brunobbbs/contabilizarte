from django.test import TestCase
from contabilizarte.theme.models import SpecialCategory, ImportantLinks


class SpecialCategoryTest(TestCase):
    def setUp(self):
        SpecialCategory.objects.create(
            title='Contabilidade na Prática',
            url='http://www.contabilizarte.com.br',
            active=True,
        )

    def test_model(self):
        self.assertTrue(SpecialCategory.objects.exists())

    def test_important_links_display_on_home_if_active(self):
        SpecialCategory.objects.create(
            title='Job Dicas',
            url='http://www.contabilizarte.com.br/category/job-dicas',
            active=False,
        )
        resp = self.client.get('/')
        self.assertNotContains(
            resp,
            '<a href="http://www.contabilizarte.com.br/category/job-dicas"',
        )
        self.assertContains(
            resp,
            '<a href="http://www.contabilizarte.com.br"',
        )


class ImportantLinksTest(TestCase):
    def setUp(self):
        ImportantLinks.objects.create(
            title='ContabiliZarte',
            url='http://www.contabilizarte.com.br',
            active=True,
        )

    def test_model(self):
        self.assertTrue(ImportantLinks.objects.exists())

    def test_important_links_display_on_home_if_active(self):
        ImportantLinks.objects.create(
            title='GitHub do Bruno',
            url='https://github.com/brunobbbs',
            active=False,
        )
        resp = self.client.get('/')
        self.assertContains(
            resp,
            '<a href="http://www.contabilizarte.com.br"',
        )
        self.assertNotContains(
            resp,
            '<a href="https://github.com/brunobbbs"',
        )
