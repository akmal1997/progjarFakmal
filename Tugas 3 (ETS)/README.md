# Tugas 3 Pemrograman Jaringan (ETS)

Akmal Darari Rafif Baskoro
<br>
05111640000148 / Departemen Informatika / Progjar F
<br>
Institut Teknologi Sepuluh Nopember
<br>
Surabaya, Jawa Timur

## Penjelasan:

![Gambar 1](https://raw.githubusercontent.com/akmal1997/progjarFakmal/master/Tugas%203%20(ETS)/media/gambar1.jpg)

Dalam screenshot ini, adalah pengetesan jika semisal client mencoba koneksi dengan server jika server tidak tersambung

![Gambar 2](https://raw.githubusercontent.com/akmal1997/progjarFakmal/master/Tugas%203%20(ETS)/media/gambar2.jpg)

Untuk percobaan, saya memasukkan beberapa file yang tersedia (Dalam kasus ini, saya memasukkan file berformat .jpg .mp4 .mp3 .txt)

Terdapat beberapa sintaks pada program:
<br>
<br>
ls: Untuk list semua file yang ada di server
<br>
get: Untuk mendownload file dari server ke client
<br>
put: Untuk mengupload file dari client ke server
<br>
rm: Untuk delete file
<br>
quit: Untuk keluar dari program (dua-duanya) dan memutuskan koneksi client dan server
<br>
help: Untuk bantuan dan memunculkan command yang tersedia

## Cara Menjalankan:

Untuk user Ubuntu atau Linux Debian based, cukup mengetik "python client.py" (untuk client, terdapat didalam folder client) dan "python server.py" (untuk server) di Terminal


## Pengetesan:

Saya mencoba mendownload file stainless.jpg, edsheeranperfect.MP4, bleedinglove.txt, dan pasrah.mp3

Untuk hasil, semuanya bisa. Namun, hanya saja program ini memiliki kekurangan untuk nama file wajib sama persis termasuk ekstensinya (case sensitive). Saya sudah mencobanya untuk mendownload file edsheeranperfect.mp4, jika diinput ekstensinya dengan huruf kecil, maka tidak akan bisa didownload. Namun, jika diinput ekstensinya sesuai nama file (yaitu .MP4), file bisa didownload. Untuk file, tidak ada yang corrupt sama sekali termasuk juga file audio dan video yang sudah saya sertakan

Untuk mengupload ke server, saya mencoba upload file perfect.txt. Hasilnya bisa dan lancar

Untuk file yang ada di client, sudah saya masukkan di folder client

Terima Kasih.


