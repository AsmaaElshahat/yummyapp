from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'ingredients', 'steps', 'duration', 'servings']
    list_filter = ['slug']
