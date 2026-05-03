from django.contrib import admin
from .models import Vehicle, VehicleMaintenance, OilChange

admin.site.register(Vehicle)
admin.site.register(VehicleMaintenance)
admin.site.register(OilChange)
