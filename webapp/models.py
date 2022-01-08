from django.db import models
from django.contrib.gis.db import models

class Weather(models.Model):
    city_name           = models.CharField(max_length = 1000 , null = True , blank = True)
    latitude            = models.CharField(max_length = 1000 , null = True , blank = True)
    longitude           = models.CharField(max_length = 1000 , null = True , blank = True)
    location            = models.PointField(null=True, blank=True)
    temperature         = models.CharField(max_length = 100  , null = True , blank = True)
    humidity            = models.CharField(max_length = 100  , null = True , blank = True)
    created_at          = models.DateField(auto_now_add=True)
    status              = models.BooleanField(default=True)

    def __str__(self):
        return self.city_name

