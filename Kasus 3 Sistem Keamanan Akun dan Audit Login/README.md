Kasus 3: Sistem Keamanan Akun dan Audit Login

Masalah yang Diselesaikan:
Verifikasi login harus memakai aturan format yang ketat, dan setiap percobaan login (berhasil maupun gagal) harus tercatat otomatis tanpa mengotori logika otentikasi.

Aturan validasi:
- Username: minimal 5 karakter, hanya huruf dan angka (tanpa spasi atau simbol).
- Password: minimal 8 karakter dan memuat minimal satu angka.

Konsep Python yang Digunakan:
1. RegEx (re): digunakan untuk [A-Za-z0-9]{5,} untuk username dan (?=.*\d).{8,} untuk password, dicocokkan dengan fullmatch
2. @property + setter: digunakan untuk Class User memvalidasi username dan password saat diisi; password disimpan sebagai hash SHA-256
3. Decorator & closure: digunakan untuk @audit_log membungkus login() dan mencatat waktu, username, status BERHASIL/DITOLAK beserta alasannya

Fungsi login() hanya berisi logika otentikasi. Pencatatan log sepenuhnya ditangani decorator, sehingga kodenya tetap bersih.

Cara Menjalankan:
Syarat utamanya harus Python 3.8 atau lebih baru (hanya library standar).

cd case-03-login-security
python main.py

Program juga menulis riwayat ke file audit.log di folder yang sama (dibuat otomatis, tidak perlu di-commit).

Skenario Pengujian
- Username ab! -> ditolak (format username salah)
- Password abc12 -> ditolak (terlalu pendek)
- Password passwordku -> ditolak (tidak ada angka)
- Password salahsalah9 -> ditolak (format benar, tetapi tidak cocok)
- Username aisyah01 + password rahasia123 -> BERHASIL

Contoh Output:
Timestamp akan berbeda setiap kali dijalankan.

Skenario 1: username tidak sesuai aturan
[2026-10-10 16:37:29] user='ab!' status=DITOLAK (Username minimal 5 karakter, hanya huruf dan angka)

Skenario 2a: password terlalu pendek
[2026-10-10 16:37:29] user='aisyah01' status=DITOLAK (Password minimal 8 karakter)

Skenario 2b: password tanpa angka
[2026-10-10 16:37:29] user='aisyah01' status=DITOLAK (Password harus mengandung minimal satu angka)

Skenario 3a: format benar, tapi password salah
[2026-10-10 16:37:29] user='aisyah01' status=DITOLAK (Username atau password salah)

Skenario 3b: semua kriteria terpenuhi
[2026-10-10 16:37:29] user='aisyah01' status=BERHASIL

Riwayat tersimpan di 'audit.log'