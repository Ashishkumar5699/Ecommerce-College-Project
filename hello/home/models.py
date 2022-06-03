from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=122)
    Email = models.EmailField()
    Phone = models.CharField(max_length=122)
    Desc = models.TextField()
    Date = models.DateField()

    def __str__(self):
        return self.Name 

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default = "")
    subcategory = models.CharField(max_length=50, default = "")
    price = models.IntegerField(default = 0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default = "")

    def __str__(self):
        return self.product_name

class user(models.Model):
    
    

    def __str__(self):
        return self.product_name

    



