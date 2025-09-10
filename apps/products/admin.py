from django.contrib import admin

from .models import (
    ProductCategory, ProductColor, ProductCatalog,
    ProductModel, ProductQuantity, ProductImageModel
)


class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    extra = 1  # Number of empty forms to display
    fields = ['image']
    verbose_name = 'Product Image'
    verbose_name_plural = 'Product Images'


class ProductQuantityInline(admin.TabularInline):
    model = ProductQuantity
    extra = 1  # Number of empty forms to display
    fields = ['quantity', 'colors']
    verbose_name = 'Product Quantity'
    verbose_name_plural = 'Product Quantities'


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'catalog', 'price', 'discount']
    list_filter = ['catalog', 'categories', 'created_at']
    search_fields = ['title', 'short_description']
    filter_horizontal = ['categories']

    inlines = [ProductImageInline, ProductQuantityInline]

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'long_description', 'image')
        }),
        ('Product Details', {
            'fields': ('categories', 'catalog', 'price', 'discount')
        }),
    )


# Register other models normally
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ['title', 'code']
    search_fields = ['title', 'code']


@admin.register(ProductCatalog)
class ProductCatalogAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']
    search_fields = ['title']