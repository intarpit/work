from django.contrib import admin
from .models import wash_basin

# * Create class here
class wash_basin_view(admin.ModelAdmin):
    list_display = ['item_name', 'brand', 'price']



# * Register your models here.

admin.site.register(wash_basin, wash_basin_view)
