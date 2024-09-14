from django.db import models

class RegionalInformation(models.Model):
    lat = models.FloatField()  # Latitude
    lng = models.FloatField()  # Longitude
    month = models.PositiveIntegerField()  # Month (1-12)
    year = models.PositiveIntegerField()  # Year
    min_temp = models.FloatField()  # Minimum Temperature
    max_temp = models.FloatField()  # Maximum Temperature
    avg_temp = models.FloatField()  # Average Temperature
    total_perception = models.FloatField()  # Total Precipitation

    def __str__(self):
        return f"{self.year}-{self.month} | Lat: {self.lat}, Lng: {self.lng}"
    
class Seeds(models.Model):
    name = models.CharField(max_length=100)  # Name of the seed
    min_temp = models.FloatField()  # Minimum Temperature required
    max_temp = models.FloatField()  # Maximum Temperature required
    min_rainfall = models.FloatField()  # Minimum Rainfall required
    max_rainfall = models.FloatField()  # Maximum Rainfall required
    min_ph_soil = models.FloatField()  # Minimum Soil pH required
    max_ph_soil = models.FloatField()  # Maximum Soil pH required

    def __str__(self):
        return self.name
