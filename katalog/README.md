# Tugas 2 PBP
Link deploy: https://tugas-2-pbp-raudhatul-jannah.herokuapp.com/katalog/

## Flowchart
![messageImage_1663210854140](https://user-images.githubusercontent.com/94220270/190304200-e636614f-d512-4fc9-86fa-e63a2f9c0abb.jpg)

Web aplikasi tersebut dapat dibuat karena adanya request oleh user yang selanjutnya diproses oleh middlewares yang akan diteruskan ke URL router. Setelah itu, URLS akan memanggil function pada views.py setelah memeriksa request yang diberikan memiliki handler. Web aplikasi akan memberikan query request ke models.py yang kemudian akan diteruskan ke database. Database akan me-return data yang ada ke models.py dan kemudian me-return ke views.py. Data yang sudah ada pada views.py akan digunakan untuk template. Web aplikasi akan merespon request yang diberikan user berupa bentuk file html.


## VIRTUAL ENVIRONMENT
Virtual environment adalah tools yang bisa digunakan dalam membuat space terpisah untuk suatu proyek bisa memasang dependensi, packages, dan versi yang diperlukan proyek tersebut agar kemungkinan adanya konflik package di global environment bisa dieliminasi. Virtual environment digunakan untuk mengisolasi suatu proyek dengan proyek yang lain dan bisa membantu proyek yang sedang kita kerjakan bisa dikerjakan oleh orang lain dengan mudah. Kita tetap bisa mengerjakan suatu proyek tanpa virtual environment. Kelemahannya adalah package yang diinstall akan tersimpan di global environment.

## CARA IMPLEMENTASI POIN 1-4
### 1. Membuat fungsi show_katalog yang menerima request dan me-return nilai dari fungsi render() pada views.py yang ada di app katalog.
- Mengimport fungsi render() dan model class
- Mengambil seluruh list object yang ada di fungsi show_katalog
- Membuat variabel yang akan me-return data ke template berupa dictionary
- Me-return hasil pemanggilan fungsi render()
### 2. Melakukan routing fungsi yang sudah di views.py pada urls.py
- Menambahkan routing pada path(...) di urlpatterns di folder katalog > urls.py
- Menambahkan routing pada path(...) di urlpatterns di folder project_django > urls.py
### 3. Melakukan migrasi data dari models untuk digunakan pada template dengan memanfaatkan template yang ada
- Menambahkan tabel data yang akan menampilkan data yang ada dari list_katalog yang memiliki data initial_catalog_data.json.
- Menambahkan data diri
### 4. Melakukan deploy proyek django ke Heroku
- Salin API KEY dari akun heroku `Account Settings -> API Key`
- Buka konfigurasi repositori GitHub dan buka bagian Secrets untuk Github Actions `(Settings -> Secrets -> Actions)`
- Agar bisa melakukan deployment, tambahkan variabel repository secret baru dan simpan variabel-variabel tersebut. Contohnya adalah sebagai berikut.

    `(NAME)HEROKU_APP_NAME`
    `(VALUE)APLIKASI-SAYA`

- Buka tab GitHub Actions, lalu jalankan kembali workflow yang gagal
