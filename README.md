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
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
       ```
  5. Untuk melihat dalam bentu JSON by ID, buat fungsi `show_json_by_id` pada `main.py`
       ```py
       def show_json_by_id(request, id):
            data = Item.objects.filter(pk=id)
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
      ]
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

<details>
<summary> Tugas 4 </summary>

#### Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
-  UserCreationForm adalah library bawaan Django yang digunakan untuk memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web sehingga developer tidak perlu membuat dari awal. UserCreationForm sudah berisi field untuk diisi username, password, password confirmation, serta aturan penamaan username dan password seperti melakukan register website biasa.

#### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Dalam konteks Django, autentikasi memverifikasi identitas pengguna yang mengakses webiste Django.
Sedangkan otorisasi memutuskan izin (apa saja yang diperbolehkan dan tidak diperbolehkan) pengguna yang terautensikasi tersebut.

  Penjahat siber sering mengargetkan aplikasi web untuk mengakses informasi privasi pengguna seperti keuangan. Autensikasi dan otorisasi dalam situs Django sangat penting agar menjauhkan data pengguna dari tangan hacker tersebut.

#### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

- Cookie adalah salah satu cara yang biasa aplikasi web gunakan untuk melakukan holding state. Misalnya untuk mencegah permintaan login yang berulang pada website yang sama. Cara kerja cookie adalah dengan menyimpan *session ID* pada komputer klien sebagai cookie (maksimal 4 KB). Session ID ini kemudian dipetakan ke suatu struktur data pada sisi server web misalnya username, nama, dan password. 

#### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

- Dalam kondisi default, cookie tidak dapat mentransfer malware atau virus karena data yang dibawa cookie tidak dapat berubah ketika berpindah dari komputer ke website dan sebaliknya. 

  Namun situs-situs yang mencurigakan harus diwaspadai. Misalnya website streaming ilegal yang berisi 10 iklan online. Situs web pihak ketiga yang tertaut ke iklan tersebut akan menghasilkan 100 cookie meskipun pengguna tidak pernah mengklik iklan tersebut.


#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Untuk mengimplementasi fungsi registrasi, buat function di `views.py`
   ```py
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
    ```
    Kemudian buat berkas `register.html` pada direktori main/templates yang berisi
    ```html
    {% extends 'base.html' %}
    {% block meta %}
        <title>Register</title>
    {% endblock meta %}
    {% block content %}  
    <div class = "login">
        <h1>Register</h1>  
            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>  
                </table>  
            </form>
        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}
    </div>  
    {% endblock content %}
    ```
    Terakhir, tambahkan path ke dalam urlspatterns pada `urls.py`
    ```py
    path('register/', register, name='register')
    ```

2. Untuk mengimplementasi fungsi login, buat function login_user pada `views.py`
   ```py
   def login_user(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
   context = {}
   return render(request, 'login.html', context)
   ```
   Buat file `login.html` pada folder main/templates berisi:
   ```py
   {% extends 'base.html' %}
   {% block meta %}
        <title>Login</title>
   {% endblock meta %}
   {% block content %}
   <div class = "login">
       <h1>Login</h1>
       <form method="POST" action="">
           {% csrf_token %}
           <table>
               <tr>
                   <td>Username: </td>
                   <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
               </tr>
               <tr>
                   <td>Password: </td>
                   <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
               </tr>
               <tr>
                   <td></td>
                   <td><input class="btn login_btn" type="submit" value="Login"></td>
               </tr>
           </table>
       </form>
       {% if messages %}
           <ul>
               {% for message in messages %}
                   <li>{{ message }}</li>
               {% endfor %}
           </ul>
       {% endif %}     
       Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
   </div>
   {% endblock content %}
   ```
   Jangan lupa tambahkan path login ke dalam urlpatterns pada `urls.py`
   ```py
   path('login/', login_user, name='login'), 
   ```
   Untuk merestriksi akses ke halaman main tanpa login, tambahkan kode berikut di atas function show_main pada `views.html`
   ```py
   @login_required(login_url='/login')
   def show_main(request):
   ```

3. Untuk mengimplementasi logout, buat function logout_user pada `views.py`
   ```py
   def logout_user(request):
      logout(request)
      return redirect('main:login')
   ```
   Tambahkan tombol logout pada `main.html`
   ```html
   <a href="{% url 'main:logout' %}">
      <button>
            Logout
      </button>
   </a>
   ```
   Tambahkan path pada urlpatterns pada `urls.py`
   ```py
   path('logout/', logout_user, name='logout'),
   ```

4. Untuk membuat dua akun pengguna, jalankan server di lokal kemudian klik 'Register Now' dan masukkan username dan password untuk membuat dua akun.

        Akun 1:
        Username: fredo1
        Password: fredomelvern

        Akun 2:
        Username: fredo2
        Password: fredomelvern
    
    Untuk membuat 3 dummy data, login terlebih dahulu ke akun yang sudah dibuat kemudian tekan tombol `Add New Item` kemudian isi field name, amount, dan description sebanyak 3 kali.


5. Menghubungkan model Item dengan User.
   Tambahkan kode berikut pada `models.py` (jangan lupa melakukan migrasi setelah mengubah konten dari model)
   ```py
   ...
   from django.contrib.auth.models import User

   class Item(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
   ```
   Kemudian mengubah function create_item pada `views.py` pada direktori main menjadi:
   ```py
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
   ```
   Untuk memfilter Item sehingga yang ditampilkan hanyalah yang dibuat oleh user dari request serta menampilakn username, ubah function `show_main` menjadi berikut
   ```py
   def show_main(request):
        items = Item.objects.filter(user=request.user)
        ...
        context = {
            ...
            'items': items,
            'user_name' : request.user.username,
        }
   ```
   serta menampilaknnya dalam `main.html`
   ```html
   <h5>Logged in as: </h5>
   <p>{{ user_name }}<p>
   ```

6. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
   Untuk menyimpan cookie last_login yang berisi waktu terakhir kali user tersebut login, tambahkan kode berikut pada function login_user pada `views.py`:
   ```py
   if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
   ```
   Untuk mengirim data cookie ke template html, tambahkan kode ini pada function show_main pada `views.py`
   ```py
   context = {
        ...
        'last_login': request.COOKIES['last_login']
   }
   ```
   Jangan lupa menampilkan data tersebut pada `main.html`
   ```html
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ```

   Untuk menghapuse cookie tersebut ketika logout, tambahkan kode berikut pada function logout_user pada `views.py`
   ```py
   def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
   ```


</details>

<details>
<summary>Tugas 5</summary>

### Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.

*Element selector* digunakan untuk memilih elemen HTML yang ingin di-style berdasarkan kategori tertentu. Element selectors dalam CSS dapat dibagi menjadi 5 macam:

- Universal selector (*)
  - Untuk memilih semua elemen di file HTML termasuk elemen di dalamnya.
  - Digunaan saat ingin men-style dasar atau menghindari styling default browser

- Simple selectors
  - Element selector:
    - Untuk memilih semua elemen dengan tipe sama (misalnya p, h1, h2)
    - Digunakan saat ingin memberi style yang seragam kepada elemen dengan tipe tertentu.
  - Id selector (#):
    - Untuk memilih elemen berdasarkan ID
    - Digunakan untuk memberi style kepada elemen yang memiliki ID unik tertentu.
  - Class selector (.):
    - Untuk memilih elemen berdasarkan nama kelasnya
    - Digunakan saat ingin memberi style yang seragam kepada elemen dengan kelas tertentu.

- Combinator selectors:
  - Untuk memilih elemen berdasarkan hubungannya dengan elemen lain.
  - Digunakan saat ingin menghubungkan dua atau lebih selector untuk merincikan lebih lanjut elemen-elemen yang ingin dipilih

- Pseudo-class selectors:
  - Untuk memilih elemen berdasarkan state tertentu, misalnya saat mouse hover di atasnya
  - Digunakan saat ingin memberi efek pada elemen ketika berinteraksi dengan pengguna.

- Pseudo-elements selectors:
  - Untuk memilih bagian spesifik dari elemen, misalnya huruf pertama.
  - Digunakan saat ingin menambahkan styling tambahan pada elemen
- Attribute selectors ([attribute]):

  - Untuk memilih elemen dengan atribut HTML tertentu.
  - Digunakan saat ingin memilih elemen yang memiliki atribut tertenty, misalnya  `input[type="text"]`.


### Jelaskan HTML5 Tag yang kamu ketahui.

- title: mendefinisikan judul halaman yang ditampilkan di tab browser.
- style: untuk menempatkan kode CSS langsung di dalam dokumen HTML.
- body: elemen yang berisi semua konten yang akan ditampilkan di halaman web
- article: menggambarkan sebuah konten independen yang bisa berdiri sendiri, seperti posting blog atau artikel berita.
- footer: mengatur bagian bawah halaman.
- video: memasukkan pemutar video dalam halaman web.
- audio: memasukkan pemutar audio dalam halaman web.
- input: untuk membuat input form, seperti teks, kata sandi, radio button, checkbox
- button: untuk membuat tombol yang dapat diklik oleh pengguna.
- div: untuk mengelompokkan elemen HTML.
- h1, h2, .., h6: header dan subheader

### Jelaskan perbedaan antara margin dan padding.

**Margin**
- digunakan untuk menata letak dari sisi luar
- biasanya tidak memiliki warna

**Padding**
- digunakan untuk menata letak dari sisi dalam
- bisa menggunakan unsur warna sesuai dengan warna background halamannya


### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?

Tailwind CSS:
- desain fleksibel dan memungkinkan membangun tampilan dengan cara yang lebih terperinci.
- tampilan dapat dikonfigurasi dengan cepat dan mudah.
- ukuran file lebih ringan karena hanya memuat style yang digunakan
- Digunakan ketika membutuhkan tingkat kostumisasi yang tinggi dan mengurangi penumpukan berkas yang tidak digunakan.

Bootsrap:
- desain yang lebih terstruktur dan telah mendefinisikan gaya tampilan yang lebih kohesif. Menggunakan kelas CSS yang sudah memiliki style yang ditentukan.
- kustomisasinya mungkin memerlukan penyesuaian lebih lanjut.
- ukuran file besar karena sudah termasuk banyak komponen dan gaya yang berbeda.
- digunakan untuk membangun prototype dengan cepat tanpa menulis kode CSS dan dengan gaya yang sudah ditentukan.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-stepas

Untuk membuat navigation bar, saya terlebih dahulu membuat ordered list dengan html kemudian distyle dengan css sebagai berikut
  ```html
  <ul class="my-navbar">
    <li class="nama-aplikasi">{{nama_aplikasi}}</li>
    <li class="user-name">
      Welcome, {{user_name}}
      <a href="{% url 'main:logout' %}"> Logout </a>
    </li>
  </ul>
  ```
  ```css
            ul.my-navbar{
                list-style-type: none;
                margin: 0;
                padding: 13px;
                background-color: #001524;
                overflow: hidden;
                
                color: #FDE5D4;
                

                display: flex;
                justify-content: space-between;
                align-items: center;
                
                top: 0;
                width: 100%;
                position: sticky;
            }
            li.nama-aplikasi
                font-weight:600;
                font-size:25px;
            li a{
                color: #FDE5D4;
                text-decoration: none;
                padding-left: 15px;
            }
            li a:hover{
                color: #FDE5D4;
                text-decoration: underline;
            }
  ```

Untuk membuat desain halaman login dan register, saya menamakan mereka sebagai class `login` dan register dengan id `register` kemudian di-style dengan css:
```css
            .login{
                display: flex;
                flex-direction: column;
                align-items: center;
                text-align: center;
            }
            .login table{
                width: 400px;
                height: 200px;
                
                border-radius: 20px;
                background-color: #D6CC99;
                margin: 40px;
            }
            .login td{
                
                padding: 20px;
            }
            #register table{
                width: 600px;
            }
            #register ul{
                text-align: left;
            }
```
Untuk kostumisasi halaman daftar inventory menjadi lebih berwarna saya memasukkan tabel ke dalam class `styled-table` kemudian di-style dengan css sebagai berikut (kode css ini juga mengimplementasi bonus task untuk memberi warna teks dan background pada baris terakhir tabel):
```css
            .styled-table {
                width: 100%;
                font-size: 1em;
                border: 1px solid #001524;
            }
            .styled-table th, .styled-table td {
                padding: 12px 15px;
            }
            .styled-table th {
                background-color: rgb(33, 29, 29);
                color: #fdd300;
            }
            .styled-table tr:nth-child(even) {
                background-color: #D6CC99;
            }
            .styled-table tr:nth-child(odd) {
                background-color: #c3b983;
            }
            .styled-table tr:last-child{
                color:yellow;
                font-weight: 600;
                background-color: #c8b966;
            }
            .styled-table tr:hover {
                background-color: #d8c45e;
            }
```
</details>

<details>
<summary>Tugas 6</summary>

### Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronous programming menjalankan fungsi berurutan, artinya agar dapat menjalankan fungsi berikutnya, program harus menunggu fungsi sebelumnya selesai. Aprroach ini dapat mengakibatkan waktu tunggu yang lama jika ada salah satu tugas yang memakan waktu lama.

Sedangkan syncrhonous programming tidak menjalankan fungsi secara berulutan, artinya kita tidka perlu mengunggu suatu fungsi selesai dijalankan untuk menjalankan fungsi lainnya. Approach ini berguna dalam situasi di mana ingin menjalankan beberapa tugas secara bersamaan atau saat ada tugas yang harus menunggu sumber daya eksternal, seperti permintaan HTTP atau akses database.

### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven programming adalah pendekatan dalam pemrograman di mana alur eksekusi program tidak ditentukan oleh urutan kode yang telah ditulis, tetapi oleh peristiwa (event) yang terjadi pada waktu tertentu.

Dalam konteks JavaScript dan AJAX, penerapan event-driven programming sangat berguna karena banyak interaksi pengguna atau komunikasi dengan server yang berdasarkan event.

Contohnya pada tugas ini: penggunaan event listener onClick pada button dengan id `button_add` yang akan memanggil function `addItem()` bila ada event ditekan.
  ```js
  document.getElementById("button_add").onclick = addItem
  ```

### Jelaskan penerapan asynchronous programming pada AJAX.

AJAX (Asynchronous JavaScript and XML) menggunakan asynchronous programming pada data transfer (HTTP request) antara browser dan web server. Hal ini memungkinkan browser mengambil data dari server secara asynchronous tanpa menghentikan eksekusi kode JavaScript utama maupun me-refresh halaman browser. Sebaliknya, aplikasi akan tetap responsif dan dapat menjalankan tugas-tugas lain sambil menunggu respons dari server.


### Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Fetch API:
- murni javascript, tidak perlu menggunakan library external
- cocok untuk membangun website berukuran kecil
- membuat request dengan Promise dengan async, await, dan then()
- mendukung berbagai jenis permintaan HTTP, termasuk GET, POST, PUT, DELETE serta mengatur header permintaan, jenis data yang dikiri, dll
- Tidak hanya mengambil data dari AJAX, fetch API juga mengambil sumber daya dari server seperti RESTful API atau JSON

jQuery
- perlu mengunduh library jQuery
- cocok untuk membangun website berukuran besar
- API kaya dan lengkap dalam melakukan operasi AJAX
- mendukung cross-browser yang memudahkan dalam menangani masalah kompatibilitas
- menyederhanakan kode yang dibutuhkan untuk melakukan permintaan AJAX dibandingkan dengan fetch API

Menurut saya sebagai mahasiswa, teknologi yang lebih baik digunakan adalah Fetch API karena menggunakan library yang sudah built-in, tidak perlu mengunduh dari library eksternal. Selain itu untuk pemula, membangun website ringan dan berukuran kecil saja sudah cukup.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Untuk mengimplementasi AJAX dalam membuat sistem refresh tabel, membuat item baru, mengincrement amount, decrement amount, serta remove item, pertama-tama saya membuat 5 function yang diperlukan nanti `views.py`
  ```py
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
  ```
Kemudian saya menghubungkan kelima function tersebut ke dalam `urlpatterns`
  ```py
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('add-ajax/', add_ajax, name='add_ajax'),
    path('remove-ajax/', remove_ajax, name='remove_ajax'),
    path('remove-all-ajax/', remove_all_ajax, name='remove_all_ajax'),
  ```
Karena data tabel berubah dari yang awalnya berasal dari context menjadi data dari fetch API, maka tabel yang lama saya hapus, diganti menjadi 1 line seperti berikut:
  ```html
  <table id="item_table" class="styled-table"></table>
  ```

Untuk membuat tombol modal degnan form untuk menambahkan item, saya menghapus tombol add new item yang lama dan menggantinya menjadi:
```html
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Item by AJAX</button>
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Item</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="price" class="col-form-label">Amount:</label>
                        <input type="number" class="form-control" id="amount" name="amount"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Item</button>
            </div>
        </div>
    </div>
</div>
```

Setelah saya membuat semua function yang diperlukan, membuat tabel kosong, serta menyiapkan modal. Sekarang yang dilakukan adalah membuat JavaScript di bawah main.html agar semua elemen tersebut berjalan dengan baik.
```html
<script>
    async function getItems() {
        return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
    }
    async function refreshItems() {
        const items = await getItems()
        let htmlString = `<tr>
            <th>Name</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Date Added</th>
            <th>Add 1</th>
            <th>Remove 1</th>
            <th>Remove All</th>
        </tr>`

        items.forEach((item) => {
            htmlString += `\n<tr>
            <td>${item.fields.name}</td>
            <td>${item.fields.amount}</td>
            <td>${item.fields.description}</td>
            <td>${item.fields.date_added}</td>
            <td><button class="edit" onclick="addItemAmount(${item.pk})">+</button></td>
            <td><button class="edit" onclick="removeItemAmount(${item.pk})"">-</button></td>
            <td><button class="edit" onclick="removeItem(${item.pk})">X</button></td>
        </tr>` 
        })
        document.getElementById("item_table").innerHTML = htmlString
    }

    refreshItems()

    function addItem() {
        
        fetch("{% url 'main:create_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshItems)

        document.getElementById("form").reset()
        return false
    }

    document.getElementById("button_add").onclick = addItem

    function addItemAmount(pk){

        const formData = new FormData()
        formData.append("id", pk)

        fetch("{% url 'main:add_ajax' %}",{
            method: "POST",
            body: formData
        }).then(refreshItems)
    }

    function removeItemAmount(pk){

        const formData = new FormData()
        formData.append("id", pk)

        fetch("{% url 'main:remove_ajax' %}",{
            method: "POST",
            body: formData
        }).then(refreshItems)

        return false
    }
    function removeItem(pk){

        const formData = new FormData()
        formData.append("id", pk)

        fetch("{% url 'main:remove_all_ajax' %}",{
            method: "POST",
            body: formData
        }).then(refreshItems)

        return false
    }
</script>
```
Untuk mengumpulkan file static dari setiap aplikasi ke dalam suatu folder yang dapat dengan mudah disajikan pada produksi, saya menulis line baru pada `settings.py`:
   ```py
   STATIC_ROOT = BASE_DIR / 'productionfiles'
   ```
Kemudian menjalankan command 
   ```
   python manage.py collectstatic
   ```
</details>