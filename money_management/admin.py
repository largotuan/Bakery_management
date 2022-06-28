from django.contrib import admin
from money_management.models import Category, Transaction
# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {
            'fields': ['created_by', 'category', 'amount', 'note'],
            'classes': ('collapse',),
        }),
    ]
    list_display = ['id', 'category', 'name', 'amount', 'note']
    list_display_links = ['id', 'category', 'name']


class TransactionInLine(admin.TabularInline):
    model = Transaction
    extra = 1
    fields = ['name', 'amount', 'note', 'created_at']
    readonly_fields = ['created_at']

    class Meta:
        ordering = ['created_at']


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {
            'fields': ['name']
        }),
    ]

    list_display = ['name']
    list_display_links = ['name']

    inlines = [TransactionInLine]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Transaction, TransactionAdmin)

