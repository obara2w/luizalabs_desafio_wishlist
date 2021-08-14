from django.contrib import admin

from api.models import Customer, Wishlist, Product


class WishlistInline(admin.TabularInline):
    model = Wishlist
    fields = ['product']
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'name', 'email')
    fields = ['name', 'email', ]
    search_fields = ['name', 'email']
    inlines = [WishlistInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ('id', 'title', 'brand', 'price', 'image')
    fields = ['title', 'brand', 'price', 'image', 'review_score']
    list_filter = ('brand', )
    search_fields = ['title', 'brand']
