from django.contrib import admin

from .models.aboutus import (
    AboutUs,
    Foreword)

from .models.category import Category
from models.sponsors import Partner
from .models.success_story import SuccessStory, Author
from .models.carousel_headers import CarouselHeader


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated', 'active']

    search_fields = ['title', 'active']
    readonly_fields = ('created', 'updated',)


class ForewordAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created', 'updated', 'active']

    search_fields = ['title', 'owner', 'active']
    readonly_fields = ('created', 'updated',)


class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'updated', 'published']

    search_fields = ['title', 'author', 'category']
    readonly_fields = ('created', 'updated',)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'active']


admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Foreword, ForewordAdmin)
admin.site.register(SuccessStory, SuccessStoryAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Category)
admin.site.register(CarouselHeader)
admin.site.register(Author)

# class smartcareAdmin(admin.ModelAdmin):
#     list_display = ['code', 'name', 'brand']
#     search_fields = ['code', 'name', 'brancd']
#     readonly_fields = ['created', 'updated']
#     fieldsets = (
#         ('Main details', {
#             'fields': ('code', 'name', 'brand', )
#         }),
#         ('Other properties', {
#             'classes': ('collapse',),
#             'fields': ('created', 'updated',),
#         }),
#     )
# admin.site.register(smartcare, smartcareAdmin)
