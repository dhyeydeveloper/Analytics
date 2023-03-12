from django.contrib import admin
from .models import BitcoinTracking

class BitcoinTrackingAdmin(admin.ModelAdmin):
    list_display = ["mytimestamp","price"]

admin.site.register(BitcoinTracking, BitcoinTrackingAdmin)