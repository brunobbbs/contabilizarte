from django.contrib import admin
from contabilizarte.theme.models import SpecialCategory, ImportantLinks


class SpecialCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'active')


class ImportantLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'active')


admin.site.register(SpecialCategory, SpecialCategoryAdmin)
admin.site.register(ImportantLinks, ImportantLinksAdmin)
