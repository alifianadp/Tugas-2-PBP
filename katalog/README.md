Link Heroku : https://tugas2-catalog-pbp.herokuapp.com

## Pertanyaan
1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
    Bagan : https://drive.google.com/file/d/1Dzx0DSyPz06HAE-rU-JbC70vq29e2HCP/view?usp=sharing
    Ketika client request ke web aplikasi, HTTP request akan dipetakan dalam URLS dan diteruskan ke VIEW. Pada VIEW request diproses dan akan memanggil MODEL untuk membaca/menulis data ke database. Selanjutnya, VIEW akan memanggil TEMPLATE yaitu katalog.html untuk merender data dalam format tertentu (jsonn) dan mengirimkannya dalam bentuk HTTP ke client.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Kita memerlukan virtual environment untuk mengisolasi package serta dependencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer. Di samping itu, kita masih dapat membuat aplikasi web berbaris Django tanpa virtual environtment, tetapi akan ada kemungkinan versi yang digunakan akan berubah sehingga aplikasi tidak lagi dapat dijalankan dan membutuhkan kode yang baru.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
    1) Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
        Pertama import models yang digunakan dalam hal ini adalah class CatalogItem pada file models.py.
        Setelah itu, membuat fungsi pada views.py yang menerima parameter request dan mengembalikan :
        return render(request, "katalog.html", context)
        Fungsi tersebut berfungsi untuk memanggil fungsi query ke model database dan menyimpannya ke dalam variabel.
    2) Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
        Pada file urls.py folder aplikasi katalog kita dapat melakukan import path dan show_katalog.
        Selanjutnya, kita dapat menuliskan variabel nama aplikasi yang diinginkan berserta urlpatterns yang ada.
        Selain itu, pada file urls folder project_django kita juga perlu menambahkan path pada variabel urlpatterns.
    3) Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
        Kita dapat mengisi katalog.html dengan variabel-variabel yang sudah dibuat sebelumnya dalam hal ini nama, npm, dan barang-barang yang ada.
        Untuk sintaks Django dalam pemetaan data template kita dapat menggunakan : {{ VARIABEL }}
    4) Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
        Pertama, membuat aplikasi pada website Heroku dan menyalin API key dari akun berserta informasi mengenai aplikasi
        Selanjutnya, menambahkan variabel repository secret pada GitHub berdasarkan informasi yang sebelumnya (Name-Value)
        Setelah variabel disimpan, membuka GitHub Actions dan menjalankan workflow yang gagal


