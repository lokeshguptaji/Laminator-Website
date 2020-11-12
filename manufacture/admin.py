from django.contrib import admin
from .models import Items,Contact

# Register your models here.
admin.site.register((Items,Contact))