from django.shortcuts import render, get_object_or_404

from .models import Cover

def pianocovers(request):
    covers = Cover.objects.all().order_by('cover_id')
    return render(request, 'covers/pianocovers.html', {'covers':covers})

def guitarcovers(request):
    covers = Cover.objects.all().order_by('cover_id')
    return render(request, 'covers/guitarcovers.html', {'covers':covers})

def coverdetail(request, cover_id):
    detailcover = get_object_or_404(Cover, pk=cover_id)
    return render(request, 'covers/coverdetail.html', {'cover':detailcover})
