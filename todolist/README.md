# TUGAS 4

## LINK DEPLOYMENT
https://tugas-2-pbp-raudhatul-jannah.herokuapp.com/todolist

### Apa kegunaan {% csrf_token %} pada elemen `<form>?` Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?
  csrf merupakan jenis token yang bisa dihasilkan oleh server ketika end-user ingin merender halaman form dan memastikan setiap permintaan yang masuk untuk diperiksa apakah sesuai dengan token yang dihasilkan. Permintaan tidak akan bisa dieksekusi jika permintaan yang diberikan tidak berisi token. Jika tidak ada potongan kode tersebut pada elemen `<form>`, maka akan menghasilkan error yang menyebabkan halaman HTML tidak bisa muncul. Selain itu, serangan dari luar juga bisa saja terjadi jika potongan kode tersebut tidak ada.

### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti `{{ form.as_table }})`? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.
Kita bisa membuat elemen `<form>` secara manual dengan cara membuat elemen `<form>`. Caranya hanya dengan menambahkan hal-hal yang ingin dimasukkan, seperti ingin membuat tabel, memasukkan input text, dan lainnya. Elemen `<input>` bisa digunakan untuk mendapatkan input dari pengguna, seperti input username dan password. 

### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
1. Ketika user mengklik tombol submit form, maka data akan dapat diakses menggunakan HTTP req POST dan akan dikirimkan ke server.
2. Pada HTTP req yang didapat, server akan memeriksa datanya valid atau tidak.
3. Bila datanya valid, data tersebut akan disimpan di database, kemudian kita bisa mengakses data tersebut sesuai dengan kebutuhan yang ingin kita akses.
4. Masukkan ke context pada views, dan views akan mengembalikan atau melakukan loop HTTP response dan template HTML yang sesuai ke user. 

### Cara Implementasi
1. Membuat aplikasi django bernama todolist dengan perintah python manage.py startapp todolist di folder tugas Django yang sudah saya gunakan sebelumnya.
2. Mendaftarkan aplikasi todolist yang sudah dibuat ke dalam variabel INSTALLED_APPS yang ada di settings.py pada folder project_django. Kemudian, menambahkan path todolist di urls.py pada folder project_django untuk melakukan routing ke urls di todolist.
3. Membuat model task di models.py dan membuat user fieldnya berupa foreginkey ke user.
4. Melakukan implementasi form registrasi, login, dan logout di views.py. 
5. Membuat halaman HTML yang menampilkan tabel to do list, tombol tambah task, dan tombol logout. Kemudian membuat templatenya pada todolist.html
6. Membuat halaman form agar user bisa menambahkan task.
7. Membuat template create.html untuk menambahkan task dengan input yang diminta yaitu Title dan description. Kemudian ada tombol Tambah untuk menyimpan  data yang di input.
8. Melakukan routing pada tiap fungsi yang telah dibuat pada urls.py dengan menambahkan path.
9. Melakukan deploy ke heroku.
10. Membuat 2 akun dan membuat minimal 3 dummy to do list pada masing-masing akun


# TUGAS 5
## Perbedaan Inline, Internal, dan External CSS
`Inline` ->
Style hanya berada di satu elemen saja

#### Kelebihan
- Mempercepat perbaikan
- Mempermudah ketika ingin menguji style pada satu elemen
- Mempercepat load pada halaman web

#### Kekurangan
Tidak efisien karena hanya berada di satu elemen saja

`Internal` ->
CSS berada di file yang sama
#### Kelebihan
Hanya bisa berlaku di satu halaman saja
#### Kekurangan
Tidak efisien jika ingin menggunakan style yang sama di file yang berbeda

`Eksternal` ->
CSS berada di file sendiri
#### Kelebihan
File CSS lebih efisien karena berada dalam satu file yang sama dengan HTML
#### Kekurangan
Halaman HTML akan berantakan jika CSS tidak berhasil dipanggil dan file akan menjadi lebih banyak

## TAG HTML5 yang diketahui
- `html>` -> Tag untuk membuat dokumen HTML
- `<title>` -> Tag untuk menentukan judul dari suatu halaman
- `<body>` -> Tag untuk membuat tubuh dari suatu halaman
- `<h1> - <h6>` -> Tag untuk membuat header
- `<p>` -> Tag untuk membuat suatu paragraf
- `<a>` -> Tag untuk membuat hyperlink
- `<br>` -> Tag untuk memberikan satu baris kosong
- `<b>` -> Tag untuk membuat suatu kata tercetak tebal
- `<table>` -> Tag untuk membuat table
- `<th>` -> Tag untuk membuat caption pada table
- `<tr>` -> Tag untuk membuat baris pada table
- `<td>` -> Tag untuk membuat sel pada table
- `<form>` -> Tag untuk membuat form untuk input user
- `<input>` -> Tag untuk membuat suatu input
- `<button>` -> Tag untuk membuat suatu tombol yang bisa diklik
- `<label>` -> Tag untuk membuat label
- `<img>` -> Tag untuk memasukkan gambar

## Tipe-tipe CSS Selektor
- `.Class` -> Selektor untuk memilih elemen berdasarkan class yang dipilih
- Tag -> Selektor untuk memilih elemen berdasarkan tag
- Universal( * ) -> Selektor untuk memilih semua elemen pada scope tertentu
- #ID -> Selektor untuk memilih elemen berdasarkan ID dan hanya bisa digunakan satu elemen

## Cara Implementasi
1. Menerapkan style dan bootstrap di `add_task.html`, `login.html`, `register.html`, dan `todolist.html` pada folder `templates` yang ada di `todolist`
2. Memasukkan bootsrap pada `base.html` 
3. Memasukkan media query pada `base html` agar keempat halaman html bisa menjadi responsif
4. Melakukan deploy ke heroku
