from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh', 'Andhra Pradesh' ),
    ('Arunachal', 'Arunachal'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chattisgarh', 'Chattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli' ),
    ('Daman and Diu', 'Daman and Diu' ),
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Gujrat', 'Gujrat'),
    ('Haryana', 'Haryana'),
    ('Himachal', 'Himachal'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerla', 'Kerla'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab', 'Punjab',),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
)
# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES, max_length=50)

    def __srt__(self):
        return str(self.id)

CATEGORY_CHOICES = (
('M', 'Mobile'),
('TW', 'Top Wear'),
('BW', 'Bottom Wear')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices = CATEGORY_CHOICES, max_length = 2)
    product_image = models.ImageField(upload_to = 'productimg') 

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return str(self.id)
@property
def total_cost(self):
    print(self.quantity * self.Product.discounted_price)
    return self.quantity * self.product.discounted_price
    return self.title

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The way'),
    ('Delivered', 'Delivered'),
    ('Cencel', 'Cencel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    ordered_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 50, choices = STATUS_CHOICES, default = 'Pending')
