from django.db import models
from django.db import models

class Product(models.Model):
    name = models.CharField('nome', max_length=255)
    price = price = models.DecimalField(
        'preço',
        max_digits=5,
        decimal_places=2,
        default=0.0
    )
    score = models.IntegerField('score')
    image = models.ImageField('imagem')    
    freight = models.DecimalField(
        'frete',
        max_digits=5,
        decimal_places=2,
        default=10.0
    )
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100, default= None, null=True, blank=True)
    last_name = models.CharField(max_length=100, default= None, null=True, blank=True)
    email = models.EmailField(max_length=100, default= None, null=True, blank=True, unique=True)


    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField('nome', max_length=255)
    price = price = models.DecimalField(
        'preço',
        max_digits=5,
        decimal_places=2,
        default=0.0
    )
    score = models.IntegerField('score')
    image = models.ImageField('imagem')    
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, null = True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    freight = models.DecimalField(
        'frete',
        max_digits=5,
        decimal_places=2,
        default=10.0
    )  

    @property
    def num_of_items(self):
        cartitems = self.cartitems_set.all()
        qtysum = sum([ qty.quantity for qty in cartitems])
        return qtysum
    
    @property
    def cart_total(self):
        cartitems = self.cartitems_set.all()
        qtysum = sum([ qty.subtotal for qty in cartitems])
        return qtysum
    
    @property
    def cart_checkout(self):
        if self.cart_total >=250:
            self.freight = 0
        checkout = self.cart_total + self.freight        
        return checkout   
    

    def __str__(self):
        return str(self.completed)

class Cartitems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.IntegerField(default=0)   
    
    @property
    def subtotal(self):
        subtotal = self.quantity * self.product.price        
        return subtotal
    
    @property
    def total(self):
        if subtotal >= 250.00:
            freight = 0
        total =  subtotal + freight
        return total

    def __str__(self):
        return str(self.quantity)
   

class SavedItem(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, null = True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    added = models.IntegerField(default=0)
    
    
    
    def __str__(self):
        return str(self.id)

class Order(models.Model):
    customer = models.ForeignKey(
        Customer,
        verbose_name='cliente',
        on_delete=models.CASCADE,
        null=True
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)    
    paid = models.BooleanField('pago?', default=False)    
    created = models.DateTimeField('criado em', auto_now_add=True)
    updated = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'{str(self.pk).zfill(3)}'


class OrderItems(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name='ordem',
        on_delete=models.CASCADE,
        null=True
    )    
    quantity = models.IntegerField('quantidade', default=1)
    price = models.DecimalField(
        'preço',
        max_digits=5,
        decimal_places=2,
        null=True,
        default=0.0
    )    
    created = models.DateTimeField('criado em', auto_now_add=True)
    updated = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        ordering = ('order', 'pk')
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'

    def __str__(self):
        return f'{self.order} {str(self.pk).zfill(3)}'



