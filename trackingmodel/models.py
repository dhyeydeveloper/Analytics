from django.db import models
from django.utils.timezone import utc
import datetime

class BitcoinTracking(models.Model): 
    mytimestamp = models.DateTimeField()
    price = models.IntegerField()
