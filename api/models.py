from django.db import models

# Create your models here
class Certificate(models.Model):
    domain = models.CharField(max_length=255)
    certificate_type = models.CharField(max_length=100)
    subscription_period = models.CharField(max_length=100)
    certificate_issued = models.DateField()

    def __str__(self):
        return self.domain


class Domain(models.Model):
    domain_name = models.CharField(max_length=255)
    auto_renew = models.CharField(max_length=10)
    lock = models.CharField(max_length=10)
    status = models.CharField(max_length=50)
    expiration_date = models.DateField()
    privacy = models.CharField(max_length=10)
    nameservers = models.TextField()
    estimated_value = models.CharField(max_length=50)
    create_date = models.DateField()
    renewal_price = models.CharField(max_length=50)
    protection_plan = models.CharField(max_length=50)
    ownership_date = models.DateField()

    def __str__(self):
        return self.domain_name



# Modelo de Marcas
class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50, blank=True, null=True)
    active = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)      # Fecha de última actualización
    
    def __str__(self):
        return self.name

# Modelo de Modelos
class Model(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")
    active = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.brand.name})"

# Modelo de Series
class Series(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="series")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="series_brand")  # Agregar referencia a Brand
    active = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)    
        
    def __str__(self):
        return f"{self.name} ({self.model.name})"

# Modelo de Categorías
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    active = models.CharField(max_length=20, default='active')
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)    
    
    def __str__(self):
        return self.name

# Modelo de Lotes (Inventory)

class Inventory(models.Model):
    batch_code = models.CharField(max_length=50, unique=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="batches")
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="batches_model")  # Relacionar con Model
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="batches_brand")  # Relacionar con Brand
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="batches_category")  # Relacionar con Category
    quantity = models.IntegerField()
    status = models.CharField(max_length=5000, default='Available')
    date_added = models.DateTimeField(auto_now_add=True)
    active = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"Batch {self.batch_code} - {self.series.name}"
