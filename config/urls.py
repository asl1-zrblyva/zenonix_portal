from django.contrib import admin
from django.urls import path
from blog.views import ana_sehife, meqale_detay
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ana_sehife, name='ana_sehife'),
    path('meqale/<int:pk>/', meqale_detay, name='meqale_detay'),
]

# Şəkillərin brauzerdə görünməsi üçün bu hissə mütləqdir
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)