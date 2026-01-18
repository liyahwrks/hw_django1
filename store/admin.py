from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description_short')
    ordering = ('name',)
    search_fields = ('name', 'description')
    search_help_text = 'Введите название категории или описание'
    
    def description_short(self, obj):
        if len(obj.description) > 50:
            return f"{obj.description[:50]}..."
        return obj.description
    
    description_short.short_description = 'Описание'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    ordering = ['-created_at', 'name']
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description', 'category__name')
    search_help_text = 'Введите название товара или описание'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'category', 'price')
        }),
        ('Описание товара', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
        ('Системная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at',)
    
    @admin.action(description='Снизить цену на 10 процентов')
    def decrease_price(self, request, queryset):
        for product in queryset:
            product.price = product.price * 0.9
            product.save()
        self.message_user(request, f'{queryset.count()} товаров обновлено')
    
    @admin.action(description='Повысить цену на 10 процентов')
    def increase_price(self, request, queryset):
        for product in queryset:
            product.price = product.price * 1.1
            product.save()
        self.message_user(request, f'{queryset.count()} товаров обновлено')
    
    actions = (decrease_price, increase_price)