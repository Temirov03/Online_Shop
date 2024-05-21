from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import *
# Register your models here.

admin.site.unregister(Group)
class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user','vendor','category','title','product_image','price','featured','product_status', 'pid']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image','cid']


class VendorAdmin(admin.ModelAdmin):
    list_display = ['title','vendor_image']


class CartOrderAdmin(admin.ModelAdmin):
    list_display = ['user','price', 'paid_status','order_date','product_status']



class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','invoice_no', 'item','image','qty', 'price','total']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product', 'review','rating']


class wishlistAdmin(admin.ModelAdmin):
    list_display = ['user','product','date']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user','address','status']



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist, wishlistAdmin)
admin.site.register(Address, AddressAdmin)


