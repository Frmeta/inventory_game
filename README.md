# Inventory: The Game
Ini adalah repository Github untuk projek Inventory: The game!
Tautan menuju aplikasi Adaptable: https://inventory-game.adaptable.app/main/

![google](https://qph.cf2.quoracdn.net/main-qimg-305c4af61154add4ecd0cb9dd99b0f18)


### Jawaban pertanyaan

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [X] Membuat sebuah proyek Django baru.
  1. Membuat direktori bernama `inventory_game`
  2. Membuat virtual environment dengan menjalankan perintah berikut di powershell
        ```
        python -m venv env
        env\Scripts\activate.bat
        ```
  3. Menyimpan nama-nama semua libary yang diperlukan dengan membuat berkas `requirements.txt`
        ```
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        ```
  4. Install semua library tersebut dengan menjalankan perintah berikut.
        ```
        pip install -r requirements.txt
        ```
  5. Membuat projek Django dengan menjalankan
        ```
        django-admin startproject inventory_game .
        ```
  6. Tambahkan * pada ALLOWED_HOSTS di `settings.py` untuk keperluan deployment
        ```python
        ALLOWED_HOSTS = ["*"]
        ```

- [X] Membuat aplikasi dengan nama `main` pada proyek tersebut.
  1. Jalankan perintah berikut di powershell
        ```
        python manage.py startapp main
        ```
  
- [X] Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
  1. Mendaftarkan aplikasi tersebut ke dalam proyek dengan menambahkan `'main'` di `INSTALLED_APPS`
        ```python
        INSTALLED_APPS = [
            ...,
            'main'
        ]
        ```

- [X] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
  * `name` sebagai nama item dengan tipe `CharField`.
  * `amount` sebagai jumlah item dengan tipe `IntegerField`.
  * `description` sebagai deskripsi item dengan tipe `TextField`.
  1. Mengisi `models.py` dengan kode berikut
        ```python
        from django.db import models

        class Item(models.Model):
            name = models.CharField(max_length=255)
            amount = models.IntegerField()
            description = models.TextField()
        ```
  2. Setiap kali melakukan perubahan model, harus melakukan migrasi dengan menjalankan perintah berikut
        ```
        python manage.py makemigrations
        python manage.py migrate
        ```
        
- [X] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
  1. Mengubah isi `views.py` yang ada di direktori aplikasi main menjadi berikut
        ```python
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
            ```

- [X] Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py`.
  1. Membuat berkas `urls.py` di dalam direktori aplikasi `main` dengan isi berikut
        ```python
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```

  2. Mengisi berkas `urls.py` di dalam direktori `inventory_game` dengan kode sebagai berikut.
        ```python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('main/', include('main.urls')),
        ]
        ```

- [X] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
  1. Lakukan `add`, `commit`, dan `push` dari direktori repositori lokal.
  2. Log in ke Adaptable.io dan pilih `New App` kemudian `Connect an Existing Repository`
  3. Hubungkan Adaptable.io dengan GitHub dan pilih All Repositories pada proses instalasi.
  4. Pilih respository proyek `inventory_game` dan branch yang ingin dideploy
  5. Pilih `Python App Template`, `PostgreSQL`
  6. Pilih versi Python yang sesuai (pada tugas ini menggunakan 3.11). Pada Start Command, masukkan perintah `python manage.py migrate && gunicorn inventory_game.wsgi`.
  7. Isi nama aplikasi dan centang bagian `HTTP Listener on PORT` dan tekan `Deploy App`.




2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.