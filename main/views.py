from django.shortcuts import render
from main.models import Item

def show_main(request):
    # Item.objects.create()
    items = Item.objects.all()
    
    context = {
        'nama_aplikasi': 'Inventory: The Game',
        'nama': 'Fredo Melvern Tanzil',
        'kelas': 'PBP D',
        'items': items,
        'items2' : [{'name' : "Pena", 'amount' : 2, 'description' : "Pena adalah alat tulis yang digunakan untuk menulis"}, 
                    {'name' : "Pensil", 'amount' : 1, 'description' : "Pensil adalah alat tulis yang digunakan untuk menulis tapi bisa dihapus"},
                    {'name' : "Penghapus", 'amount' : 1, 'description' : "Penghapus adalah alat tulis yang digunakan untuk menghapus tulisan dari pensil"}]
    }

    return render(request, "main.html", context)