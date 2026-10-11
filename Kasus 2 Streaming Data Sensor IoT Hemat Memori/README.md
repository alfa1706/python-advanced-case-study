Kasus 2: Streaming Data Sensor IoT Hemat Memori

Masalah yang Diselesaikan:
Stasiun cuaca mengirim ribuan bacaan suhu per jam. Memuat semuanya ke satu list sekaligus akan menguras memori. Program ini memproduksi dan memproses data satu per satu saat diminta (streaming), lalu mengelompokkan setiap suhu:

Kategori dan Syarat
- Dingin: suhu < 20 C
- Normal: 20 C sampai 30 C
- Panas: suhu > 30 C

Konsep Python yang Digunakan:
1. Generator function (yield): Dipakai untuk baca_sensor() menghasilkan suhu 15.0-38.0 C satu per satu
2. Iterator pattern: Dipakai untuk Konsumsi manual dengan next() dan otomatis dengan for + islice
3. Pipeline generator: Dipakai untuk stream_berstatus() menyambung aliran suhu dengan kategorinya
4. Efisiensi memori: Dipakai untuk Perbandingan sys.getsizeof list 1 juta data vs generator

Inti idenya: yield menjeda fungsi dan mengembalikan satu nilai. Fungsi baru berlanjut ketika data berikutnya diminta, jadi tidak ada list raksasa di memori.

Cara Menjalankan:
Syarat utamanya harus memakai Python 3.8 atau lebih baru (hanya memakai library standar).

cd case-02-iot-generator
python main.py

random.seed(42) dipakai agar output selalu sama saat dicoba ulang. Hapus baris itu jika ingin data acak yang berbeda setiap kali.

Contoh Output:
=== A. Konsumsi manual dengan next() ===
next() ke-1: 29.7 C -> Normal
next() ke-2: 15.6 C -> Dingin
next() ke-3: 21.3 C -> Normal

=== B. Streaming 12 pembacaan berturut-turut ===
No    Suhu (C)   Status
----------------------------
1         20.1   Normal
2         31.9   Panas
3         30.6   Panas
4         35.5   Panas
5         17.0   Dingin
6         24.7   Normal
7         15.7   Dingin
8         20.0   Normal
9         26.6   Normal
10        15.6   Dingin
11        19.6   Dingin
12        29.9   Normal

=== C. Bukti efisiensi memori (1.000.000 data) ===
List      :  8,448,728 byte (belum termasuk isi float-nya)
Generator :        224 byte