from django.db import models

STATUS_CHOICES = (
    ('Submitted', 'submitted'),
    ('Not submitted', 'not_submitted'),
)

class Contractor(models.Model):
    name = models.CharField(max_length = 100)
    nip = models.CharField(max_length = 100)
    address = models.CharField(max_length = 180)

    def __str__(self):
        return self.name

class Order(models.Model):
    contractor_id = models.ForeignKey(Contractor, on_delete = models.CASCADE) #Connection to Contractor
    implementation_date = models.DateTimeField()
    data_of_placing_the_order = models.DateTimeField()
    status = models.CharField(max_length = 13, choices = STATUS_CHOICES)
    order_value = models.DecimalField(max_digits = 30, decimal_places = 2)

class Product(models.Model):
    name = models.CharField(max_length = 100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits = 30, decimal_places = 2)
    full_price = models.DecimalField(max_digits = 30, decimal_places = 2)
    order_id = models.ForeignKey(Order, related_name = 'products', on_delete = models.CASCADE) #Connection to Order
    product_id = models.IntegerField()
