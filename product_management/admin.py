from django.contrib import admin
from product_management.models import Product, History

# Register your models here.


class HistoryInLine(admin.TabularInline):
    model = History
    extra = 0
    fields = ['price', 'type', 'quantity', 'created_at']
    # readonly_fields = ['created_at', 'price', 'subtotal']
    # ordering = ['-created_at']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Product Information', {
            'fields': ['name', 'quantity', 'price']
        }),
    ]

    list_display = ['name', 'quantity']
    list_display_links = ['name', 'quantity']

    inlines = [HistoryInLine]


class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ProductField', {
            'fields': ['product', 'quantity', 'price']
        }),

        # ('HistoryField', {
        #     'fields': ['quantity'],
        #     'classes': ('collapse',)
        # }),
    ]

    list_display = ['product', 'quantity', 'price']
    list_display_links = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(History, HistoryAdmin)
