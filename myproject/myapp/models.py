from django.db import models

class User(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    phone = models.IntegerField()
    address = models.TextField()
    
    def __str__(self):
        return f'Name: {self.name} Email: {self.email} Phone: {self.phone} Address: {self.address}'
    
class Commodity (models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField()
    
class Order (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    
