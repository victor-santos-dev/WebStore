from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    slug_product = models.SlugField(max_length=50)

    def __str__(self):

        return self.name

class ImageProduct(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField()
    
    def __str__(self):

        return self.product.name

class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    name = models.CharField(max_length=300)
    stock = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()

    class Meta:
        ordering = ('stock',)  

    @property
    def title(self):

        if not self.name:
            return self.product.name

        return self.name
    
    @property
    def discount_price(self):

        if not self.discount:

            return self.price
        
        return (self.discount*0.1)*self.price

    def __str__(self):

        return self.name

