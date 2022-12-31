# TUGAS 6

## Asynchronous Programming 
Program yang berjalan secara sekuensial dan waktu yang diperlukan untuk eksekusi cenderung lebih lambat.
Cara kerja: program dieksekusi baris per baris secara hirarki dan untuk menjalankan kode selanjutnya menggunakan proses antrian.

## Synchronous Programming
Program yang berjalan secara bersamaan dan waktu yang diperlukan untuk eksekusi lebih cepat dan lebih singkat.
Cara kerja: program dieksekusi secara bersamaan dan tidak menggunakan proses antrian

## Event-Driven Programming 
Event-Driven Programming adalah suatu paradigma pemrograman yang cara kerjanya tergantung dari suatu kejadian atau event tertentu. 
Contoh penerapannya pada tugas ini adalah ketika button di klik, maka program akan mengirimkan data task baru.

## Penerapan Ssynchronous Programming pada AJAX
Penerapan asynchronous programming pada AJAX terjadi ketika event dilakukan. Misalnya ketika tombol button di klik, program akan segera mengeksekusi suatu proses tanpa perlu menunggu proses antrian hierarki kode selanjutnya.

## Cara Implementasi
1. Menerapkan asynchronous programming untuk membuat fungsi show_json dan add_task
2. Melakukan routing show_json dan add_task di urls.py
Membuat card dengan <script> di todolist.html dan merefers ke add_task untuk membuat object task baru dan mereturn hasil POST
3. Request GET ke todolist/json, lalu map ke data. Card akan ditambahkan setiap dilakukan iterasi dan akan muncul pada halaman
4. Membuat fungsi POST yang akan berjalan ketika button TambahTask ditekan. Jika POST berhasil, maka data akan ditambahkan dengan card yang baru dibuat.
