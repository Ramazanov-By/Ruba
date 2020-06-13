from django.contrib import admin
from .models import Category, Product, ContactInfo, Banner, ProductSizes, About, Brand, Structure

class StructureAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Structure, StructureAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Brand, BrandAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'description']


admin.site.register(ContactInfo, ContactAdmin)


class ProductSizesAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(ProductSizes, ProductSizesAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'new', 'sale']
    list_filter = ['available', 'created', 'updated', 'new', 'sale']
    list_editable = ['price', 'available', 'new', 'sale']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']


admin.site.register(Banner, BannerAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']


admin.site.register(About, AboutAdmin)

