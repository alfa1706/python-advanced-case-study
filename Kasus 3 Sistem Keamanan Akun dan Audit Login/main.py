import functools
import hashlib
import re
from datetime import datetime
 
POLA_USERNAME = re.compile(r"[A-Za-z0-9]{5,}")  
POLA_PASSWORD = re.compile(r"(?=.*\d).{8,}")    
FILE_LOG = "audit.log"
 
 
class User:
 
    def __init__(self, username, password):
        self.username = username  
        self.password = password  
 
    @property
    def username(self):
        return self._username
 
    @username.setter
    def username(self, value):
        if not POLA_USERNAME.fullmatch(value):
            raise ValueError("Username minimal 5 karakter, hanya huruf dan angka")
        self._username = value
 
    @property
    def password(self):
        return self._password_hash
 
    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Password minimal 8 karakter")
        if not POLA_PASSWORD.fullmatch(value):
            raise ValueError("Password harus mengandung minimal satu angka")
        self._password_hash = self._hash(value)
 
    @staticmethod
    def _hash(teks):
        return hashlib.sha256(teks.encode()).hexdigest()
 
    def cek_password(self, teks):
        return self._hash(teks) == self._password_hash
 
 
def audit_log(func):
    @functools.wraps(func)
    def wrapper(username, password):
        berhasil, alasan = func(username, password)
        status = "BERHASIL" if berhasil else f"DITOLAK ({alasan})"
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        baris = f"[{waktu}] user='{username}' status={status}"
        print(baris)
        with open(FILE_LOG, "a", encoding="utf-8") as f:
            f.write(baris + "\n")
        return berhasil, alasan
    return wrapper
 
PENGGUNA_TERDAFTAR = {"aisyah01": User("aisyah01", "rahasia123")}
 
@audit_log
def login(username, password):
    try:
        User(username, password)       
    except ValueError as err:
        return False, str(err)
    akun = PENGGUNA_TERDAFTAR.get(username)
    if akun is None or not akun.cek_password(password):
        return False, "Username atau password salah"
    return True, "OK"
 
def main():
    open(FILE_LOG, "w").close() 
 
    skenario = [
        ("Skenario 1: username tidak sesuai aturan", "ab!", "rahasia123"),
        ("Skenario 2a: password terlalu pendek", "aisyah01", "abc12"),
        ("Skenario 2b: password tanpa angka", "aisyah01", "passwordku"),
        ("Skenario 3a: format benar, tapi password salah", "aisyah01", "salahsalah9"),
        ("Skenario 3b: semua kriteria terpenuhi", "aisyah01", "rahasia123"),
    ]
    for judul, user, pw in skenario:
        print(f"\n{judul}")
        login(user, pw)
 
    print(f"\nRiwayat tersimpan di '{FILE_LOG}'")
 
 
if __name__ == "__main__":
    main()