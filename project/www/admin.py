from django.contrib import admin
from .models import Marka, Typ, Osprzęt, Model

# Register your models here.
admin.site.register(Marka)
admin.site.register(Typ)
admin.site.register(Osprzęt)
admin.site.register(Model)