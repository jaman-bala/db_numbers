from django.contrib import admin
from .models import Category_Types, Category_Number, Category_Unaa, Add_Numbers


@admin.register(Category_Types)
class Category_Types(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "id")


@admin.register(Category_Unaa)
class Category_Unaa(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "id")


@admin.register(Category_Number)
class Category_Number(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "id")


@admin.register(Add_Numbers)
class Add_Numbers(admin.ModelAdmin):
    list_display = (
        "category_types",
        "category_unaa",
        "category_number",
        "number",
        "application",
        "is_active",
        "created",
    )
    search_fields = (
        "application",

    )
    list_filter = (
        "is_active",
        "created",
    )