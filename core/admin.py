from django.contrib import admin
from .models import Product, Order

# ProductAdmin - only valid fields
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

# OrderAdmin - include user because Order has user field
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'order_status', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('order_status', 'created_at')

# Register the models with admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
