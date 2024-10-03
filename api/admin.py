from django.contrib import admin

# Register your models here.
from .models import Certificate
from .models import Domain

admin.site.register(Certificate)
admin.site.register(Domain)