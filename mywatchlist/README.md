Link Heroku :
<p>https://tugas2-catalog-pbp.herokuapp.com/mywatchlist/html/<br>
https://tugas2-catalog-pbp.herokuapp.com/mywatchlist/json/<br>
https://tugas2-catalog-pbp.herokuapp.com/mywatchlist/xml/</p>

## Pertanyaan
1. Jelaskan perbedaan antara JSON, XML, dan HTML!
    <p>JSON (JavaScript Object Notation): JSON merupakan turunan dari Object JavaScript dengan format berbentuk text dan bersifat self-descriptive dengan data disimpan dalam bentuk key dan value.<br>
    XML (eXtensible Markup Language): XML merupakan informasi yang dibungkus di dalam tag dan bersifat self-descriptive dengan struktur seperti tree yang dimulai dari root, lalu branch, hingga berakhir pada leaves.<br>
    HTML (HyperText Markup Language): HTML merupakan markup languange untuk mendesain dokumen yang akan ditampilkan pada browser web dan menggunakan tag dalam menyatakan kode-kodenya</p>
2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    <p>Karena dalam mengembangkan suatu platform kita memerlukan data delivery untuk mengirimkan data dari satu stack ke stack lainnya.</p>
3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1) Membuat suatu aplikasi baru bernama mywatchlist di proyek Django Tugas 2 pekan lalu
       <p>Membuat folder mywatchlist menggunakan perintah "python manage.py startapp mywatchlist"<br>
       Kemudian menambahkana aplikasi mywatchlist ke dalam INSTALLED_APPS pada settings.py di folder project_django</p>
    2) Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist
       <p>Pada file urls.py folder aplikasi katalog kita melakukan import path dan show_katalog.
       Selanjutnya, kita menuliskan variabel nama aplikasi yang diinginkan berserta urlpatterns yang ada.<br>
       Selain itu, pada file urls folder project_django kita juga perlu menambahkan path pada variabel urlpatterns.</p>
    3) Membuat sebuah model MyWatchList & menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat
       <p>Pada file models.py kita melakukan import models dan membuat class yang berisi atribut-atribut seperti watched, title, rating, release_date, dan review.<br>
       Setelah membuat model kita lakukan makemirgation dan migrate untuk menerapkan skema model ke database.<br>
       Selanjutnya kita buat file json pada folder fixture yang ada di folder mywatchlist.<br>
       Pada file tersebut kita masukkan data-data berdasarkan atribut-atribut yang ada pada model.<br>
       Setelah itu lakukan perintah loaddata untuk memasukkan data ke database.</p>
    5) Mengimplementasikan sebuah fitur untuk menyajikan data yang telah dibuat sebelumnya dalam tiga format (HTML, XML, JSON)
       <p>Untuk HTML, pertama import models yang telah dibuat sebelumnya di file views.py pada folder mywatchlist.<br>
       Selanjutnya buat fungsi yang akan menerima parameter request dan mengembalikan render(request, "mywatchlist.html", context).<br>
       Buat isi fungsi yang akan memanggil fungsi query ke model database dan menyimpannya ke dalam sebuah variabel.<br>
       Setelah itu, buat berkas mywatchlist.html untuk membuat tampilan html dan lakukan routing fungsi views pada file urls.py di folder mywatchlist dan juga folder project_django.</p>
       
       <p>Untuk XML, pertama import HttpResponse dan Serializer di file views.py pada folder mywatchlist.<br>
       Selanjutnya, buat fungsi yang menerima parameter request, return HttpResponse(serializers.serialize("xml", data), content_type="application/xml"), dan buat variabel yang akan menyimpan query data.<br>
       Setelah itu, lakukan routing pada file urls.py di folder mywatchlist dan juga folder project_django.</p>
       
       <p>Untuk JSON, pada file views.py di folder mywatchlist buat fungsi yang menerima parameter request, return HttpResponse(serializers.serialize("json", data), content_type="application/json").<br>
       Setelah itu, lakukan routing pada file urls.py di folder mywatchlist dan juga folder project_django.</p>
       
    6) Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
       <p>Pertama, membuat aplikasi pada website Heroku dan menyalin API key dari akun berserta informasi mengenai aplikasi.<br>
       Selanjutnya, menambahkan variabel repository secret pada GitHub berdasarkan informasi yang sebelumnya (Name-Value).<br>
       Setelah variabel disimpan, membuka GitHub Actions dan menjalankan workflow yang gagal.</p>

## Screenshot Post Man
1. PostMan -> mywatchlist/html
    ![2022-09-22](https://user-images.githubusercontent.com/99129519/191641240-92076fc9-0bc7-4fe3-8d03-4f9fbfa17ff9.png)
2. PostMan -> mywatchlist/json
    ![2022-09-22 (1)](https://user-images.githubusercontent.com/99129519/191641406-244e3089-b099-4a77-bbad-15a8132c2583.png)
3. PostMan -> mywatchlist/xml
    ![2022-09-22 (2)](https://user-images.githubusercontent.com/99129519/191641476-a22a5f63-bf0f-44a4-82c2-9e48c777782d.png)