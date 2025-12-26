from django.db import models
from django.contrib.auth.models import User

class Makale(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)
    yazar = models.ForeignKey(User, on_delete=models.CASCADE)
    resim = models.ImageField(upload_to='makale_resimleri/', null=True, blank=True) # Bu sətiri əlavə et

    def __str__(self):
        return self.baslik