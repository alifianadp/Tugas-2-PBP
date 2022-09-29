## Link Heroku
<p>https://tugas2-catalog-pbp.herokuapp.com/todolist/</p>

## Pertanyaan
1. Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?
   <p>CSRF token berfungsi untuk menghindari malicious attack dengan cara memeriksa kembali token pada setiap request yang masuk.<br>
      Jika tidak ada potongan kode tersebut, maka suatu request ilegal dapat masuk.</p> 

2. Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.
   <p>Kita dapat membuat elemen form secara manual tanpa menggunakna generator.<br>
      Hal terserbut dilakukan dengan cara membuatnya satu persatu sesuai dengan fields yang ada.<br>
      Pada form, akan digunakan tag input untuk membuat form yang nantinya pada file views.py akan menjalankan method GET.</p>
      

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
   <p>Setelah user melakukan submisi melalui HTML form, maka request ke views.py akan terbuat untuk menyimpan data form ke database.<br>
      Selanjutnya, form akan diubah menjadi cleaned_data menggunakan is_valid() untuk dapat menjalankan save().<br>
      Kemudian, akan dilakukan redirect untuk menampilkan data tersebut ke template HTML.<br> 
      Hal ini dilakukan melalui render yang akan mengarahkan ke HTML tempat data dimunculkan.</p>

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya.
    <p>Membuat folder todolist menggunakan perintah "python manage.py startapp todolist"<br>
       Kemudian menambahkana aplikasi todolist ke dalam INSTALLED_APPS pada settings.py di folder project_django</p>

    2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
    <p>Buat file urls.py pada folder todolist kita dan lakukan import path dan show_katalog.<br>
       Selanjutnya, kita menuliskan variabel nama aplikasi yang diinginkan berserta urlpatterns kosong untuk menampilkan views show_todolist.<br>
       Selain itu, pada file urls folder project_django kita juga perlu menambahkan path pada variabel urlpatterns /todolist untuk menampilkan urls pada todolist.</p>

    3. Membuat sebuah model Task
    <p>Pada file models.py kita melakukan import models dan membuat class yang berisi atribut-atribut seperti user, date, title, dan description.<br>
       Setelah membuat model kita lakukan makemirgation dan migrate untuk menerapkan skema model ke database.<br>

    4. Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
    <p>Untuk form registrasi, pertama import redirect, UserCreationForm, dan messages pada file views.py.<br>
       Kemudian, tambahkan fungsi register yang menerima parameter request.<br>
       Fungsi ini akan membuat sebuah variabel form menggunakan UserCreationForm().<br>
       Di samping itu, fungsi ini juga akan menyimpan form yang telah terisi juga memberikan messages dan akan menredirect ke login.</p>
       
    <p>Untuk implementasi login, pertama lakukan import authenticate dan login pada file views.py.<br>
       Kemudian, tambahkan fungsi login yang menerima parameter request.<br>
       Fungsi ini akan melakukan atentikasi pengguna yang akan login menggunakan username dan password.<br>
       Di samping itu, fungsi ini akan mengirimkan messages ketika password salah dan akan menredirect ke show_todolist.</p>

    <p>Untuk implementasi logout, pertama import logout pada file views.py.<br>
       Kemudian, tambahkan fungsi logout yang menerima parameter request.<br>
       Fungsi ini akan melakukan logout dan menredirect ke login.</p>

    5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
    <p>Pertama, buat file todolist.html pada folder templates di folder todolist.<br>
       Kemudian buat heading yang akan memuat judul halaman dan username pengguna.<br>
       Selain itu, buat tabel dengan header pada row pertama berisi title dari data yang akan ditampilkan<br>
       Selanjutnya, untuk row selanjutnya menggunakan for loop sebanyak data yang ada berisi date, title, description, dan button.<br>
       Di luar tabel juga tambahkan button untuk menambahkan task dan logout user.</p>

    6. Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
    <p>Pertama, buat file addtask.html pada folder templates di folder todolist.<br>
       Kemudian, buat section add_task menggunakan tag div dan buat heading dan tampilkan form dalam bentuk table.<br>

    7. Membuat routing sehingga beberapa fungsi dapat diakses melalui URL
    <p>Pertama import fungsi-fungsi yang ada pada file views.py pada file urls.py di folder todolist.<br>
       Setelah itu, tambahkan path url pada urspatterns yang ada pada urls.py di folder todolist.</p>

    8. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    <p>Pertama, membuat aplikasi pada website Heroku dan menyalin API key dari akun berserta informasi mengenai aplikasi.<br>
       Selanjutnya, menambahkan variabel repository secret pada GitHub berdasarkan informasi yang sebelumnya (Name-Value).<br>
       Setelah variabel disimpan, membuka GitHub Actions dan menjalankan workflow yang gagal.</p>

    9. Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
    <p>Buka link heroku, kemudian klik buat akun untuk membuat akun.<br>
       Kemudian login menggunakan akun yang telah dibuat dan klik tambah task baru untuk menambahkan dummy data.</p>
