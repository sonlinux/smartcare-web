from django.contrib import admin

from .models.aboutus import (
    AboutUs,
    Foreword)

class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated', 'active']

    search_fields = ['title', 'active']
    readonly_fields = ('created', 'updated',)

class ForewordAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created', 'updated', 'active']

    search_fields = ['title', 'owner', 'active']
    readonly_fields = ('created', 'updated',)

admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Foreword, ForewordAdmin)

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
