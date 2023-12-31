import datetime
import json
from django.shortcuts import render, redirect
from main.models import Item
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from main.forms import ItemForm
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    items_amount = len(items)
    
    context = {
        'nama_aplikasi': 'Inventory: The Game',
        'nama': 'Fredo Melvern Tanzil',
        'kelas': 'PBP D',
        'items_amount': items_amount,
        'items': items,
        'last_login': request.COOKIES['last_login'],
        'user_name' : request.user.username,
        'user' : request.user
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)

        # Mengisi field user dari objek item dengan user yang sedang login
        item.user = request.user
        item.save()

        # Mengeluarkan pesan sukses menyimpan item
        item_name = form.cleaned_data['name']
        item_amount = form.cleaned_data['amount']
        messages.success(request, f"Kamu berhasil menyimpan {item_name} sebanyak {item_amount}.")
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add(request, id):
    a = Item.objects.get(pk=id)
    a.amount += 1
    a.save()
    return redirect('main:show_main')

def remove(request, id):
    a = Item.objects.get(pk=id)
    a.amount -= 1
    a.save()

    if (a.amount <= 0):
        a.delete()

    return redirect('main:show_main')

def remove_all(request, id):
    a = Item.objects.get(pk=id)
    a.delete()
    return redirect('main:show_main')

def get_item_json(request):
    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def create_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def add_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id");
        a = Item.objects.get(pk=id)
        a.amount += 1
        a.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def remove_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id");
        a = Item.objects.get(pk=id)
        a.amount -= 1
        a.save()

        if (a.amount <= 0):
            a.delete()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def remove_all_ajax(request):
    if request.method == 'POST':
        id = request.POST.get("id");
        a = Item.objects.get(pk=id)
        a.delete()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


# Flutter
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    
    else:
        return JsonResponse({"status": "error"}, status=401)

#@csrf_exempt
@login_required
def get_flutter(request):
    items = Item.objects.filter(user=request.user)
    return JsonResponse(serializers.serialize('json', items), content_type="application/json")