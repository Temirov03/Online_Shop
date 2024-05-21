from django.urls import path
from core.views import *


app_name = 'core'   

urlpatterns = [
    path("",index, name='index'),
    path("products/", product_list_view, name="product-list"),
    path('product/<pid>/', product_detail_view,name='product-detail'),
    path("category/", category_list_view, name="category-list"),
    path('category/<cid>/', category_product_list_view, name='category-product-list'),
    path('vendor/', vendor_list_view, name="vendor-list"),
    path('vendor/<vid>/', vendor_detail_view, name="vendor-detail"),
    path('products/tag/<slug:tag_slug>/', tag_list, name="tags"),
    path('ajax-add-review/<int:pid>/', ajax_add_review, name='ajax-add-review'),
    path('search/', search_view, name='search'),
    path('filter-products/', filter_product, name='filter-products'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('cart/',cart_view,name='cart')
]
