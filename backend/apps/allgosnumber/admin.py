from django.contrib import admin
from .models import Category_Region, Category_Number, Category_Unaa, Add_Numbers


@admin.register(Category_Region)
class Category_Region(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("regions",)}
    list_display = ("regions", "id")


@admin.register(Category_Unaa)
class Category_Unaa(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("units",)}
    list_display = ("units", "id")


@admin.register(Category_Number)
class Category_Number(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("numbers",)}
    list_display = ("numbers", "id")


@admin.register(Add_Numbers)
class Add_Numbers(admin.ModelAdmin):
    list_display = (
        "category_region",
        "category_unaa",
        "category_number",
        "title",
        "is_active",
        "created",
    )
    search_fields = (
        "title",

    )
    list_filter = (
        "is_active",
        "created",
    )