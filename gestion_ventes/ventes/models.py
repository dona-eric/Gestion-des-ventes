from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, Group, Permission

# Create your models here.

# creation des models comme table de base de données pour la gestion des socks et ventes
# models of Products, Sales and Users

# models Users
class User(AbstractUser):
    role_choices = [('owner', 'Administrateur'), ('employee', "Employé")]
    user = models.CharField(max_length=100, choices=role_choices, default='Admin')
    email=models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name="custom_user_group", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du produit")
    description = models.TextField(verbose_name="decrire le produit", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="prix de l'article") # prix de l'article
    total_stocks = models.PositiveIntegerField() # total de stocks disponibles
    min_stocks_alert = models.IntegerField(default=5)
    updated_at = models.DateTimeField(auto_now_add=True, help_text='Date de mis à jour')
    created_at = models.DateTimeField(auto_now=True)

# class of sellers
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    employee= models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    quantity_sales = models.IntegerField() #qunatitté vendue
    total_montant = models.DecimalField(max_digits=10, decimal_places=2, blank=True) # total de vente effectuée
    date_sales = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ## calcul du montant total vendues
        self.total_montant = self.product.price * self.quantity_sales
        self.product.total_stocks -= self.quantity_sales
        self.product.save()
        super().save(*args, **kwargs)

        # verification du stocks et alerte
        if self.product.total_stocks <= self.product.min_stocks_alert:
            print(f"Alert faible stocks de l'article {self.product.name}")

    def __str__(self):
        return f"Vente de {self.quantity_sales} {self.product.name} par {self.employee}"

