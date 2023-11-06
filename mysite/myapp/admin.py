from django.contrib import admin

from .models import Product, OrderDetail


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'price', 'description',)
    actions = ('make_zero',)

    def make_zero(self, request, queryset):
        queryset.update(price=0)




admin.site.register(Product, ProductAdmin)
admin.site.register(OrderDetail)

admin.site.site_header = 'E Shop App'
admin.site.site_title = 'EShop App'
admin.site.index_title = 'Admin'