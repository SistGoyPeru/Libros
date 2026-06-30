from django.contrib import admin
from .models import Book, ReadingProgress


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'status', 'is_featured', 'is_public', 'word_count', 'uploaded_at')
    list_filter = ('status', 'language', 'is_opencode_project', 'is_featured')
    search_fields = ('title', 'author')
    readonly_fields = ('file_size', 'word_count', 'page_count', 'chapter_count',
                       'character_count', 'reading_time_minutes', 'slug',
                       'uploaded_at', 'updated_at')
    list_editable = ('price', 'is_featured', 'is_public')


@admin.register(ReadingProgress)
class ReadingProgressAdmin(admin.ModelAdmin):
    list_display = ('book', 'current_percent', 'updated_at')
