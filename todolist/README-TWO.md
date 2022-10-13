## Pertanyaan
1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
    <p>Asychronus programming bersifat multi-thread sehingga program dapat berjalan secara paralel. Di samping itu, asynchronus juga bersifat non-blocking, dimana user dapat mengirimkan banyak request ke server.<br>
    Synchronus programming bersifat single-thread sehingga hanya dapat menjalankan satu program.</p>

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
    <p>Event-Driven Programming adalah paradigma pemrograman dengan alur program yang ditentukan oleh suatu event keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya.<br>
    Contohnya adalah pemunculan modal di halaman html tersebut ketika tombol Tambah Task ditekan.</p>

3. Jelaskan penerapan asynchronous programming pada AJAX.
    <p>Asynchronus programming pada AJAX berarti bahwa script akan mengirimkan request user ke server dan melanjutkan pengeksekusian tanpa menunggu respon. Sesaat setelah respon diterima, maka script akan mengeksekusi actions yang bersangkutan tanpa adanya reload/refresh page.</p>

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. AJAX GET
        <p><b>Buatlah view baru yang mengembalikan seluruh data task dalam bentuk JSON.</b><br>
        Untuk JSON, pada file views.py di folder todolist buat fungsi yang menerima parameter request, return HttpResponse(serializers.serialize("json", data), content_type="application/json").<p>

        <p><b>Buatlah path /todolist/json yang mengarah ke view yang baru kamu buat.</b><br>
        melakukan routing pada file urls.py di folder todolist dan juga folder project_django.<br>

        <p><b>Lakukan pengambilan task menggunakan AJAX GET.</b><br></p>
        
           $.get("{% url 'todolist:show_todolist_json' %}", function(data){
            for(var i = 0; i < data.length; i++){
                var status = ""
                
                if (data[i].fields.is_finished){
                    status = "Selesai"
                }
                else {
                    status = "Belum Selesai"
                }
                
                htmlString += `\n<tr>
                    <th>${data[i].fields.date}</th>
                    <th>${data[i].fields.title}</th>
                    <th>${data[i].fields.description}</th>
                    <th>${status}</th>
                </tr>`
            }

    2. AJAX POST
        <p><b>Buatlah sebuah tombol Add Task yang membuka sebuah modal dengan form untuk menambahkan task.</b><br>
              Menambahkan code berikut pada file todolist_ajax.html</p>
        
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Tambah Task</button>
             
        <p><b>Buatlah view baru untuk menambahkan task baru ke dalam database.</b><br>
              Menambahkan code berikut pada views.py</p>
        
              @login_required(login_url='/todolist/login/')
               def show_todolist_ajax(request):
                   return render(request, "todolist_ajax.html")
        
        <p><b>Buatlah path /todolist/add yang mengarah ke view yang baru kamu buat.</b><br>
               Menambahkan code berikut pada urls.py</p>
               
               path('add/', add_task_ajax, name='add_task_ajax')
               
        <p><b>Hubungkan form yang telah kamu buat di dalam modal kamu ke path /todolist/add</b><br>
               Tambahkan code berikut ke dalam script pada file todolist_ajax.html</p>
               
               $(document).on('submit', '#form_add', function(e) {
                 e.preventDefault()
                 loadTable()
                 $.ajax({
                     type:"POST",
                     url:"{% url 'todolist:add_task_ajax' %}",
                     data:{
                         date:$("#date").val(),
                         title:$("#title").val(),
                         description:$("#description").val(),
                         is_finished:$("#is_finished").val(),
                         csrfmiddlewaretoken:'{{ csrf_token }}',
                     },
                     dataType: 'json',
                 })
                 document.getElementById("form_add").reset()
                 loadTable()
             })
        
        <p><b>Tutup modal setelah penambahan task telah berhasil dilakukan.</b><br>
               Tambahkan code berikut ke dalam button submit dalam form tambah task</p>
               
               data-bs-dismiss="modal"
        
        <p><b>Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan list terbaru tanpa reload seluruh page.</b><br>
               Lakukan pemanggillan function loadTable() untuk menampilkan table todolist yang terdaftar</p>