from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Tag, Post, Recipe, Comment


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "category", "author", "create_at"]
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "prep_time", "cook_time", "post"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "website", "create_at"]


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Tag)
