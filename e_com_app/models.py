from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        attributes = vars(self)
        attributes_string = ', '.join([f"{key}: {value}" for key, value in attributes.items()])
        return f"CustomUser({attributes_string})"

class Product(models.Model):
    label = models.CharField(max_length=50, default='', unique=True)
    price = models.FloatField(default=0.0)
    manufacturingDate = models.DateField(default=timezone.now)
    stock = models.PositiveSmallIntegerField(default=0)
    photo = models.ImageField(
        upload_to='static/photos/product_photo', null=True, blank=True)
    description = models.TextField(
        max_length=200, default='', blank=True, null=True)
    productlink=models.CharField( max_length=50, null=True)
    
    class Meta:
        db_table = 'product'

    def __str__(self):
        return f'label={self.label}'

# Update related_name for groups and user_permissions fields in the CustomUser model
CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'

class Panier(models.Model): 
    quantity = models.PositiveSmallIntegerField(default=1)
    prix_totale = models.FloatField(default=0.0)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='products_user', null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Meta:
        db_table = 'panier'

        def __str__(self):
         return f'quantity={self.quantity}'