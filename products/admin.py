from django.contrib import admin
from baseDB.models import Product, Kind, CpuKind, Brand, Category, OtherCharacteristics

# Register your models here.

admin.site.register(Product)
admin.site.register(Kind)
admin.site.register(CpuKind)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(OtherCharacteristics)