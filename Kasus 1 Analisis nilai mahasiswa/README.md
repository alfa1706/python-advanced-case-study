Kasus 1: Analisis Nilai Mahasiswa

Masalah yang Diselesaikan:
Bagian akademik menerima data nilai mahasiswa dalam bentuk list of dictionary mentah. Program ini:

1. menghitung nilai akhir dengan bobot Tugas 30%, UTS 30%, UAS 40%;
2. memfilter mahasiswa yang berprestasi (nilai akhir di atas 80);
3. membuat ranking dari nilai tertinggi ke terendah;
4. mengumumkan mahasiswa terbaik beserta NIM dan rincian nilainya.

Semua dilakukan tanpa perulangan for bertingkat.

Konsep Python yang Digunakan:

1. List comprehension: digunakan untuk	Menghitung nilai akhir semua mahasiswa dan memfilter yang berprestasi, contoh didalam code: "[m for m in data if m["nilai_akhir"] > batas]"
2. Lambda function: digunakan untuk Rumus nilai akhir dan kunci pengurutan, contoh didalam code:	"key=lambda m: m["nilai_akhir"]"
3. Filtering & sorting: digunakan untuk Ranking dari tertinggi ke terendah, contoh didalam code: "sorted(data, key=..., reverse=True)"
4. Dictionary unpacking: digunakan untuk Menambah kunci nilai_akhir tanpa mengubah data asli, contoh didalam code: "{**m, "nilai_akhir": ...}"

Cara Menjalankan:

Syaratnya harus Python 3.8 atau lebih baru.

cd case-01-analisis-nilai
python main.py

Contoh Output: 

=== 1. NILAI AKHIR SEMUA MAHASISWA ===
No  Nama      NIM       Tugas   UTS   UAS   Akhir
-------------------------------------------------
1   Aisyah    230101       85    80    88   84.70
2   Budi      230102       70    65    75   70.50
3   Cantika   230103       90    85    92   89.30
4   Dimas     230104       78    82    80   80.00
5   Eka       230105       60    70    65   65.00

=== 2. MAHASISWA BERPRESTASI (nilai akhir > 80) ===
Aisyah (84.70), Cantika (89.30)

=== 3. RANKING (tertinggi -> terendah) ===
No  Nama      NIM       Tugas   UTS   UAS   Akhir
-------------------------------------------------
1   Cantika   230103       90    85    92   89.30
2   Aisyah    230101       85    80    88   84.70
3   Dimas     230104       78    82    80   80.00
4   Budi      230102       70    65    75   70.50
5   Eka       230105       60    70    65   65.00

=== 4. MAHASISWA TERBAIK ===
Nama              : Cantika
NIM               : 230103
Tugas / UTS / UAS : 90 / 85 / 92
Nilai Akhir       : 89.30

Catatan: Dimas mendapat tepat 80,00 sehingga tidak termasuk berprestasi, karena syaratnya "di atas 80" (strictly greater).