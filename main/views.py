from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'nama aplikasi': 'Inventory: The Game',
        'nama': 'Fredo Melvern Tanzil',
        'kelas': 'PBP D'
    }

    return render(request, "main.html", context)