BOBOT = {"tugas": 0.30, "uts": 0.30, "uas": 0.40}
BATAS_BERPRESTASI = 80
 
data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 60, "uts": 70, "uas": 65},
]
 
 
def hitung_nilai_akhir(data):
    hitung = lambda m: round(sum(m[k] * b for k, b in BOBOT.items()), 2)
    return [{**m, "nilai_akhir": hitung(m)} for m in data]
 
 
def filter_berprestasi(data, batas=BATAS_BERPRESTASI):
    return [m for m in data if m["nilai_akhir"] > batas]
 
 
def buat_ranking(data):
    """Urutkan dari nilai akhir tertinggi ke terendah."""
    return sorted(data, key=lambda m: m["nilai_akhir"], reverse=True)
 
 
def cetak_tabel(data):
    print(f"{'No':<4}{'Nama':<10}{'NIM':<9}{'Tugas':>6}{'UTS':>6}{'UAS':>6}{'Akhir':>8}")
    print("-" * 49)
    for i, m in enumerate(data, start=1):
        print(f"{i:<4}{m['nama']:<10}{m['nim']:<9}{m['tugas']:>6}{m['uts']:>6}"
              f"{m['uas']:>6}{m['nilai_akhir']:>8.2f}")
 
 
def main():
    hasil = hitung_nilai_akhir(data_mahasiswa)
 
    print("=== 1. NILAI AKHIR SEMUA MAHASISWA ===")
    cetak_tabel(hasil)
 
    print(f"\n=== 2. MAHASISWA BERPRESTASI (nilai akhir > {BATAS_BERPRESTASI}) ===")
    berprestasi = filter_berprestasi(hasil)
    print(", ".join(f"{m['nama']} ({m['nilai_akhir']:.2f})" for m in berprestasi)
          or "Tidak ada")
 
    print("\n=== 3. RANKING (tertinggi -> terendah) ===")
    ranking = buat_ranking(hasil)
    cetak_tabel(ranking)
 
    print("\n=== 4. MAHASISWA TERBAIK ===")
    terbaik = ranking[0]
    print(f"Nama              : {terbaik['nama']}")
    print(f"NIM               : {terbaik['nim']}")
    print(f"Tugas / UTS / UAS : {terbaik['tugas']} / {terbaik['uts']} / {terbaik['uas']}")
    print(f"Nilai Akhir       : {terbaik['nilai_akhir']:.2f}")
 
 
if __name__ == "__main__":
    main()
 