from django.contrib import admin
from .models import Patient,Post,Category

# Register your models here.
admin.site.register(Patient)
admin.site.register(Post)
admin.site.register(Category)