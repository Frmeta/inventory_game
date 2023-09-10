from django.shortcuts import render
from main.models import Item

def show_main(request):
    # Item.objects.create()
    items = Item.objects.all()
    
    context = {
        'nama_aplikasi': 'Inventory: The Game',
        'nama': 'Fredo Melvern Tanzil',
        'kelas': 'PBP D',
        'items': items
    }

    return render(request, "main.html", context)