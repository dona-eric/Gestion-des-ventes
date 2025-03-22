from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

#User = get_user_model()
# creation des models comme table de base de données pour la gestion des socks et sales
# models of Products, Sales and Users

# models Users
class User(AbstractUser):
    role_choices = [('owner', 'Owner'), ('employee', "Employee")]
    user = models.CharField(max_length=100, choices=role_choices, default='Admin')
    email=models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name="custom_user_group", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="name of product", help_text="nom du produit")
    description = models.TextField(verbose_name="describe of product", help_text="decrire le produit",null=True)
    price_unit = models.DecimalField(max_digits=10, decimal_places=2, help_text="price of articles")
    total_stocks = models.PositiveIntegerField(help_text="Total de stocks disponibles pour ce produit")
    min_stocks_alert = models.IntegerField(default=5, help_text="stocks pour la zone d'alerte")
    updated_at = models.DateTimeField(auto_now_add=True, help_text='Date de mis à jour')
    created_at = models.DateTimeField(auto_now=True, help_text="Date d'aout du produit")

# class of sellers
class Sale(models.Model):
    METHOD_PAYMENT =[
        ('CREDIT CARD', 'Card Bank'),
        ('CASH',"Cash"),
        ('mobile_money',"MOBILE MONEY")
    ]

    STATUS_PAYMENT = [
        ('paid', 'PAID'),
        ('pending', "En Attente")
    ]
    method_payment = models.CharField(max_length=20, choices=METHOD_PAYMENT, default="Cash")
    status_payment = models.CharField(max_length=10, choices=STATUS_PAYMENT, default='PAID')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    employee= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="Celui/celle ui a vendu le produit")
    quantity_sales = models.IntegerField(help_text='quantité vendue') #quantitté vendues
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, blank=True, help_text="total rpice des articles vendues") # total de sales saved
    date_sales = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ## calcul du mont total sales
        self.total_sales = self.product.price_unit * self.quantity_sales
        self.product.total_stocks -= self.quantity_sales
        self.product.save()
        super().save(*args, **kwargs)

        # verification du stocks et alert
        if self.product.total_stocks <= self.product.min_stocks_alert:
            print(f"Alert under stocks articles {self.product.name}")

    def __str__(self):
        return f"Sales of  {self.quantity_sales} {self.product.name} par {self.employee}"


# models for return the products if the customer isn't satisfied
class Return(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    reason = models.CharField(max_length=500)
    date_return = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # update the stock quantity if return is true
        self.sale.product.quantity +=self.quantity
        self.sale.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"THe products {self.sale.name} because {self.reason}"
