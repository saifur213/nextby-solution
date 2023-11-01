from django.contrib import admin
from .models import Package,CustomUser,Contact

# Register your models here.
admin.site.register(Package)
admin.site.register(CustomUser)
admin.site.register(Contact)