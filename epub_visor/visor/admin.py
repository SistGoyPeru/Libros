from django.contrib import admin
from .models import Book, ReadingProgress, Cart, CartItem, Order, OrderItem


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


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ('book', 'quantity', 'subtotal')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total', 'created_at')
    inlines = [CartItemInline]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('book', 'price', 'quantity', 'subtotal')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'total', 'status', 'paid_at', 'created_at')
    list_filter = ('status', 'country')
    search_fields = ('full_name', 'email', 'user__username')
    list_editable = ('status',)
    readonly_fields = ('stripe_payment_intent', 'paid_at', 'created_at')
    inlines = [OrderItemInline]


admin.site.register(CartItem)
admin.site.register(OrderItem)
