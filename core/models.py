from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

STATUS_CHOICES = (
    ('process', "Processing"),
    ('shipped', "Shipped"),
    ('delivered', "Delivered"),
)


STATUS = (
    ('draf', "Draft"),
    ('disabled', "Disabled"),
    ('rejected', "Rejected"),
    ('in_review', "In Review"),
    ('published', "Published"),
)


RATING = (
    (1, "⭐✩✩✩✩"),
    (2, "⭐⭐✩✩✩"),
    (3, "⭐⭐⭐✩✩"),
    (4, "⭐⭐⭐⭐✩"),
    (5, "⭐⭐⭐⭐⭐"),
)


def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=30,prefix='cat', alphabet="aderekijru12345")
    title = models.CharField(max_length=100, default = "Food")
    image = models.ImageField(upload_to='category', default='category.jpg')


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))
    
    def __str__(self):
        return self.title
    
class Tags(models.Model):
     pass
    

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=30,prefix='ven', alphabet="aderekijru12345")

    title = models.CharField(max_length=100, default="Nestify")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    cover_image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    description = models.TextField(null=True, blank=True, default = "I am Amazing Vendor")
    description = RichTextUploadingField(null=True, blank=True, default = "I am Amazing Vendor")

    address = models.CharField(max_length=100, default="123 Main Street.")
    contact = models.CharField(max_length=100, default="+123 515 515")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")
    date = models.DateTimeField(auto_now=True, null=True,blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    class Meta:
            verbose_name = 'Vendor'
            verbose_name_plural = "Vendors"


    def vendor_image(self):
            return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))
        
    
    def __str__(self):
            return self.title
    


class  Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=30, alphabet="aderekijru12345")
     
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,related_name='category')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True,related_name="product")
    
    title = models.CharField(max_length=100, default="Fresh Pear")
    images = models.ImageField(upload_to=user_directory_path)
    description = models.TextField(null=True, blank=True, default = "This is product")

    description = RichTextUploadingField(null=True, blank=True, default = "This is product")


    price = models.DecimalField(max_digits=10, decimal_places=2, default="2.66")
    old_price = models.DecimalField(max_digits=225, decimal_places=2, default="4.66")

    specifications = models.TextField(null=True, blank=True)
    specifications = RichTextUploadingField(null=True, blank=True)     
    type = models.CharField(max_length=100, default="Organi",null=True,blank=True)   
    stock_count = models.CharField(max_length=100, default="10", null=True,blank=True)
    life = models.CharField(max_length=100, default="100 Days", null=True,blank=True)
    mfd = models.DateTimeField(auto_now_add=False, null=True,blank=True)
    tags = TaggableManager(blank=True)

    product_status = models.CharField(choices=STATUS, max_length = 100, default = "in review")


    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)



    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix = 'sku',alphabet="123456789")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Product'
            verbose_name_plural = "Products"


    def product_image(self):
            return mark_safe('<img src="%s" width="50" height="50"/>' % (self.images.url))
        
    
    def __str__(self):
            return self.title
    

    def get_precentage(self):
        new_price = (self.price/self.old_price)*100
        return new_price
    

class ProductImages(models.Model):
    images = models.ImageField(upload_to='product-images', default='product.jpg')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='p_images', null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
            verbose_name = 'Product Images'
            verbose_name_plural = "Product Images"



##################################### Cart, Order, OrderITems and Address ############################################
##################################### Cart, Order, OrderITems and Address ############################################
##################################### Cart, Order, OrderITems and Address ############################################


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=2, decimal_places=2, default="2.66")
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICES, max_length = 30, default = "processing")


    class Meta:
            verbose_name = 'Cart Order'
            verbose_name_plural = "Cart Orders"



class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE, null=True)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length = 200)
    item = models.CharField(max_length = 200)
    image = models.CharField(max_length = 200)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default="2.66")
    total = models.DecimalField(max_digits=10, decimal_places=2, default="2.66")


    class Meta:
            verbose_name = 'Cart Order Item'
            verbose_name_plural = "Cart Order Items"
    
    def order_img(self):
            return mark_safe('<img src="/media/%s" width="50" height="50"/>' % (self.image))
    

##################################### Product Review, wishlists,Address ################################################################################# Cart, Order, OrderITems and Address ############################################
##################################### Product Review, wishlists,Address ############################################
    


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField(choices = RATING, default=None)
    date =  models.DateTimeField(auto_now_add=True)


    class Meta:
            verbose_name = 'Product Revie'
            verbose_name_plural = "Products Reviews"

    
    def __str__(self):
            return self.product.title
    
    def get_rating(self):
        return self.reting
    


class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    reting = models.IntegerField(choices = RATING, default=None)
    date =  models.DateTimeField(auto_now_add=True)


    class Meta:
            verbose_name = 'Wishlist'
            verbose_name_plural = "Wishlists"
    
    def __str__(self):
            return self.product.title
    
    def get_rating(self):
        return self.reting
    


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
            verbose_name = 'Address'
            verbose_name_plural = "Address"

    