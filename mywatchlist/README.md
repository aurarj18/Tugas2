## PERBEDAAN JSON, XML, DAN HTML 
**JSON** adalah singkatan dari JavaScript Object Notation yang merupakan suatu format yang memiliki fungsi untuk menyimpan dan membaca informasi dan data dari server web. 

**XML** adalah singkatan dari Extensible Markup Language yang merupakan suatu format yang bisa digunakan di internet, World Wide Web, dan platform lainnya. XML lebih mengutamakan dalam hal transfer data.

**HTML** adalah singkatan dari HyperText Markup Language yang merupakan bahasa standar pemrogaman untuk mengelola serangkaian data dan informasi sehingga suatu dokumen dapat diakses dan ditampilkan di Internet melalui layanan web.

## PENTINGNYA DATA DELIVERY DALAM PENGIMPLEMENTASIAN SEBUAH PLATFORM
Ketika ingin mengimplementasikan suatu stack ke stack lainnya, kita memerlukan Data Delivery. **Data Delivery** membantu kita untuk melakukan pemindahan data ke tempat yang aman secara cepat. Data delivery bisa memindahkan data ke berbagai platform, sehingga bisa diakses dengan beberapa path yang berbeda, contohnya JSON, XML, ataupun HTML.

## CARA IMPLEMENTASI CHECKLIST
1. Membuat aplikasi baru bernama `mywatchlist` dengan command `python3 manage.py startapp mywatchlist`
2. Melakukan routing pada: 
    - `urls.py` dengan menambahkan path `path('mywatchlist/', include('mywatchlist.urls'))` di `urlpatterns`.
    - Melakukan routing pada `mywatchlist/urls.py sesuai path` yang diminta
3. Membuat model mywatchlist di `mywatchlist/models.py`, yaitu watched, title, rating, release_date, dan review
4. Membuat fungsi show_mywatchlist, show_json, show_xml, dan show_html di `views.py` untuk bisa menampilkan data berdasarkan path yang sesuai
5. Melakukan migrasi model dengan menjalankan `python manage.py makemigrations` dan `python manage.py migrate` di CMD

## POSTMAN
### JSON
![json](https://user-images.githubusercontent.com/94220270/191658459-456a0c9a-eb1e-4bd9-bbd3-fb9753da02ed.png)

### XML
![xml](https://user-images.githubusercontent.com/94220270/191658452-3a435cfe-28dc-418f-a2ce-f650eeb7f7d6.png)

### HTML
![html](https://user-images.githubusercontent.com/94220270/191658444-4912cae7-2752-4830-9d98-ab6640187dfe.png)

