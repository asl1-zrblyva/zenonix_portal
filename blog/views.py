from django.shortcuts import render, get_object_or_404 # 'render' mütləq burada olmalıdır
from .models import Makale

def ana_sehife(request):
    meqaleler = Makale.objects.all()
    return render(request, 'blog/index.html', {'meqaleler': meqaleler})

def meqale_detay(request, pk):
    meqale = get_object_or_404(Makale, pk=pk)
    return render(request, 'blog/detay.html', {'meqale': meqale})