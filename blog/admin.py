from django.contrib import admin
from .models import Makale  # Nöqtə qoyduğundan əmin ol

@admin.register(Makale)
class MakaleAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'yazar', 'tarih')