from django.contrib import admin

from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id",'title','category','price')
    list_display_links=("title",)
    search_fields=("title",'category')
    list_filter=('category',) 
