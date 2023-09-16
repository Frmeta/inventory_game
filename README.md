# Inventory: The Game
Ini adalah repository Github untuk projek Inventory: The game!
Tautan menuju aplikasi Adaptable: https://inventory-game.adaptable.app/main/

![google](https://qph.cf2.quoracdn.net/main-qimg-305c4af61154add4ecd0cb9dd99b0f18)


## Jawaban Pertanyaan
<details>
<summary> Tugas 2 </summary>

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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
  3. Register model yang telah dibuat ke Django Admin dengan mengubah isi `admin.py` yang berada di direktori aplikasi `main` menjadi berikut.
        ```py
        from django.contrib import admin
        from .models import Item

        admin.site.register(Item)
        ```

- [X] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
  1. Mengubah isi `views.py` yang ada di direktori aplikasi main menjadi berikut
        ```python
        from django.shortcuts import render
        from main.models import Item

        def show_main(request):
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




### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](/PNG/bagan.png)
* Client mengakses browser melalui perangkat elektroniknya kemudian mengetik URL website yang ingin diakses dalam bentuk http://. Browser lalu mengirimkan request HTTP ke Web Server melalui World Wide Web. Setiap request dari client akan diproses pertama kali oleh `urls.py` kemudian request tersebut akan di-forward ke `views.py` yang sesuai. Setelah itu `models.py` akan melakukan transaksi data dari database sesuai permintaan kemudian mengembalikan respon data ke `views.py`. Lalu `views.py` akan mengembalikan response template HTML yang sesuai kepada client.


### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?


* Virtual Environment adalah sebuah ruang lingkup virtual yang terisolasi dari dependencies utama.

  Karena project Django yang kita buat mempunyai kebutuhan / dependencies yang berbeda-beda antara satu projek dengan lainnya dan kita ingin projek-projek tersebut berjalan pada satu sistem operasi yang sama, maka dibutuhkanlah sebuah virtual environment untuk menjalankannya secara terpisah, dimana tidak perlu merubah konfigurasi pada sistem operasi yang kita pakai.

  Kita bisa saja membuat aplikasi web Django tanpa menggunakan virtual environment sama sekali. Namun akibatnya kita hanya akan dapat menargetkan satu versi Django di satu komputer. Sehingga akan timbul masalah jika kita ingin membuat web baru menggunakan versi Django terbaru sambil tetap mempertahankan situs web lama.

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

* MVT (Model View Template) adalah konsep arsitektur yang digunakan dalam pengembangan web untuk memisahkan komponen-komponen utama dari sebuah aplikasi. Konsep ini memungkinkan pengembang web untuk mengorganisasi dan mengelola kode dengan lebih terstruktur.

* MCV (Model View Controller) adalah model yang biasa digunakan oleh pengembang software. UI (view) dan mekanisme akses data (model) berhubungan dengan erat. View tidak memiliki akses terhadap Controller.

* MVVM (Model View ViewModel) adalah gabungan dari MVC dan MVP (Model View Presenter) dimana memisahkan dengan jelas pengembangan UI dari logika bisnis dan perilaku dalam aplikasi. View memiliki akses terhadap ViewModel.


**Referensi:**
- [MVC vs MVP vs MVVM](https://agus-hermanto.com/blog/detail/mvc-vs-mvp-vs-mvvm-apa-perbedaannya-mana-yang-terbaik-diantara-ketiganya-a)
- [Difference Between MVC, MVP and MVVM Architecture Pattern in Android](https://www.geeksforgeeks.org/difference-between-mvc-mvp-and-mvvm-architecture-pattern-in-android/)

</details>

<details>
  <summary>Tugas 3</summary>

### 1. Apa perbedaan antara form POST dan form GET dalam Django?

Form POST dan form GET adalah dua metode yang digunakan dalam Django untuk mengirim data dari formulir ke server. Perbedaanya antara lain:

POST | GET
--- | ---
Mengirimkan data/nilai tanpa menampilkan nilai variabel pada URL  | menampilkan data/nilai pada URL sehingga user dapat dengan mudah memasukkan nilai variabel baru.
Lebih aman karena data tidak terlihat dalam URL       | Kurang aman karena data terlihat dalam URL
Tidak dibatasi panjang string       | Dibatasi panjang string sampai 2047 karakter
Biasanya untuk input data melalui form    | Biasanya untuk input data melalui link
Biasanya untuk mengirim data-data penting/sensitif seperti password     | Biasanya untuk mengirim data-data tidak penting/sensitif

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

- **XML (eXtensible Markup Language)** adalah format pertukaran data dengan struktur pohon yang menyajikan lapisan informasi yang dapat Anda ikuti dan baca. Pohon ini dimulai dengan elemen akar/induk sebelum memberikan informasi tentang elemen anak. XML memiliki struktur yang mirip dengan HTML yaitu menggunakan tag dan atribut untuk mengatur dan menggambarkan struktur data. XML juga menggunakan tanda akhiran, yang membuatnya menjadi lebih panjang daripada JSON.

- **JSON (JavaScript Object Notation)** adalah format pertukaran data yang menggunakan pasangan key (berupa string) dan value, sehingga membuatnya lebih padat dan lebih mudah dibaca oleh manusia. 

- **HTML (Hypertext Markup Language)** adalah bahasa markup yang digunakan untuk membangun struktur dan tampilan halaman web tapi tidak secara khusus dirancang untuk pengiriman data. Meskipun demikian HTML bisa digunakan untuk mengirim data dalam bentuk formulir atau melalui parameter URL.


### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- JSON bersifat independen dari setiap bahasa pemrograman dan merupakan output API umum dalam berbagai aplikasi.
- JSON menggunakan *syntax* yang mirip dengan bahasa pemrograman JavaScript, sehingga mudah dibaca dan ditulis baik oleh manusia maupun mesin.
- JSON merupakan opsi yang cenderung lebih baru, lebih fleksibel, dan lebih populer.
- JSON dapat merepresentasikan data yang sama dalam ukuran file yang lebih kecil untuk transfer data yang lebih cepat.
- Penguraian JSON ebih aman daripada XML

  

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [X] Membuat input form untuk menambahkan objek model pada app sebelumnya.
  1. Membuat `forms.py` pada direktori main untuk membuat struktur form
     ```py
     from django.forms import ModelForm
     from main.models import Item

     class ItemForm(ModelForm):
         class Meta:
             model = Item
             fields = ["name", "amount", "description"]
     ```
      
  2. Menambah fungsi `create_item` pada `views.py` dan import library yang diperlukan
      ```py
      from django.shortcuts import render
      from main.models import Item
      from django.http import HttpResponseRedirect, HttpResponse
      from django.core import serializers
      from main.forms import ItemForm
      from django.urls import reverse

      ...
      
      def create_item(request):
            form = ItemForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                  form.save()
                  return HttpResponseRedirect(reverse('main:show_main'))

            context = {'form': form}
            return render(request, "create_item.html", context)
      ```

  3. Pada `urls.py`, import fungsi `create_item` kemudian tambahkan pada `urlpatterns`
      ```py
      ...
      path('create-item', create_item, name='create_item'),
      ...
      ```

  4. Buat `create_item.html` pada `main/templates` yang berisi:
      ```html
      {% extends 'base.html' %} 

      {% block content %}
      <h1>Add New Item</h1>

      <form method="POST">
            {% csrf_token %}
            <table>
                  {{ form.as_table }}
                  <tr>
                        <td></td>
                        <td>
                        <input type="submit" value="Add Item"/>
                        </td>
                  </tr>
            </table>
      </form>

      {% endblock %}
      ```

- [X] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
  1. Untuk dilihat dalam format tabel HTML, ambil seluruh item dari database dengan `Item.objects.all()` kemudian masukkan sebagai value pada `context` di `views.py`
       ```py
       def show_main(request):
            items = Item.objects.all()
            
            context = {
                  'nama_aplikasi': 'Inventory: The Game',
                  'nama': 'Fredo Melvern Tanzil',
                  'kelas': 'PBP D',
                  'items': items
            }
            return render(request, "main.html", context)
       ```

     Kemudian tambahkan kode berikut pada `main.html`:
       ```html
       ...
       <table>
             <tr>
                   <th>Name</th>
                   <th>Amount</th>
                   <th>Description</th>
                   <th>Date Added</th>
             </tr>
 
             {% for item in items %}
                   <tr>
                         <td>{{item.name}}</td>
                         <td>{{item.amount}}</td>
                         <td>{{item.description}}</td>
                         <td>{{item.date_added}}</td>
                   </tr>
             {% endfor %}
       </table>
 
       <br />
 
       <a href="{% url 'main:create_item' %}">
       <button>
             Add New Item
       </button>
       </a>
 
       {% endblock content %}
       ```

  2. Untuk melihat dalam bentuk XML, buat fungsi `show_xml` pada `main.py`
       ```py
       def show_xml(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
       ```

  3. Untuk melihat dalam bentuk JSON, buat fungsi `show_json` pada `main.py`
       ```py
       def show_json(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")

       ```
  4. Untuk melihat dalam bentuk XML by ID, buat fungsi `show_xml_by_id` pada `main.py`
       ```py
       def show_xml_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
       ```
  5. Untuk melihat dalam bentu JSON by ID, buat fungsi `show_json_by_id` pada `main.py`
       ```py
       def show_json_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
       ```

- [X] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
  1. Menambahkan potongan kode berikut ke `urlpatterns` pada `urls.py`
     ```py
      urlpatterns = [
            path('', show_main, name='show_main'), # routing HTML
            path('create-item', create_item, name='create_item'),
            path ('xml/', show_xml, name='show_xml'), # routing XML
            path('json/', show_json, name='show_json'), # routing JSON
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'), # routing XML by ID
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), # routing JSON by ID
      ```


<details>
<summary>Screenshot Postman</summary>

<img href="/PNG/html.png"> </img>
HTML:
![HTML](/PNG/html.png)
XML:
![XML](/PNG/xml.png)
JSON:
![JSON](/PNG/json.png)
XML by ID:
![XML by ID](/PNG/xml_by_id.png)
JSON by ID:
![JSON by ID](/PNG/json_by_id.png)

</details>

**Referensi:**
- [Perbedaan JSON dan XML](https://aws.amazon.com/id/compare/the-difference-between-json-xml/)
</details>