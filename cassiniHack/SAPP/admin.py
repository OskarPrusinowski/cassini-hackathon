from django.contrib import admin
from .models import RegionalInformation, Seeds,Soil

@admin.register(RegionalInformation)
class RegionalInformationAdmin(admin.ModelAdmin):
    list_display = ('lat', 'lng', 'month', 'year', 'min_temp', 'max_temp', 'avg_temp', 'total_perception')

@admin.register(Seeds)
class SeedsAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_temp', 'max_temp', 'min_rainfall', 'max_rainfall', 'min_ph_soil', 'max_ph_soil')

@admin.register(Soil)
class SoilsAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_ph', 'max_ph')
