#Tugas 2 PBP
Link deploy: https://tugas-2-pbp-raudhatul-jannah.herokuapp.com/katalog/

#Flowchart
![messageImage_1663210854140](https://user-images.githubusercontent.com/94220270/190304200-e636614f-d512-4fc9-86fa-e63a2f9c0abb.jpg)
Web aplikasi tersebut dapat dibuat karena adanya request oleh user yang selanjutnya diproses oleh middlewares yang akan diteruskan ke URL router. Setelah itu, URLS akan memanggil function pada views.py setelah memeriksa request yang diberikan memiliki handler. Web aplikasi akan memberikan query request ke models.py yang kemudian akan diteruskan ke database. Database akan me-return data yang ada ke models.py dan kemudian me-return ke views.py. Data yang sudah ada pada views.py akan digunakan untuk template. Web aplikasi akan merespon request yang diberikan user berupa bentuk file html.


#VIRTUAL ENVIRONMENT
