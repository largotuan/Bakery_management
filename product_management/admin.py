from django.contrib import admin
from product_management.models import Product, History
from rangefilter.filters import DateRangeFilter
from admin_numeric_filter.admin import RangeNumericFilter
# Register your models here.


class HistoryInLine(admin.TabularInline):
    model = History
    extra = 0
    fields = ['price', 'action', 'quantity', 'created_at']
    search_fields = ['action']
    readonly_fields = ['created_at', 'price']
    ordering = ['-created_at']


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = [('price', RangeNumericFilter)]
    # list_filter = [('created_at', DateRangeFilter)]
    fieldsets = [
        ('Product Information', {
            'fields': ['name', 'quantity', 'price']
        }),
    ]

    list_display = ['id', 'name', 'price', 'quantity']
    list_display_links = ['id', 'name']

    inlines = [HistoryInLine]


class HistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('ProductField', {
            'fields': ['product', 'price']
        }),

        ('HistoryField', {
            'fields': ['action', 'quantity']
        }),
    ]

    list_display = ['id', 'created_at', 'product', 'price', 'action', 'quantity']
    list_display_links = ['id', 'product']


admin.site.register(Product, ProductAdmin)
admin.site.register(History, HistoryAdmin)
