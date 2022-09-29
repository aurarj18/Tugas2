## LINK DEPLOYMENT
https://tugas-2-pbp-raudhatul-jannah.herokuapp.com/todolist

### Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
  csrf merupakan jenis token yang bisa dihasilkan oleh server ketika end-user ingin merender halaman form dan memastikan setiap permintaan yang masuk untuk diperiksa apakah sesuai dengan token yang dihasilkan. Permintaan tidak akan bisa dieksekusi jika permintaan yang diberikan tidak berisi token. Jika tidak ada potongan kode tersebut pada elemen <form>, maka akan menghasilkan error yang menyebabkan halaman HTML tidak bisa muncul. Selain itu, serangan dari luar juga bisa saja terjadi jika potongan kode tersebut tidak ada.
