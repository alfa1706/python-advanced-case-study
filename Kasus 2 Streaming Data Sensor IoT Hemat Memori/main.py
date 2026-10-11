import random
import sys
from itertools import islice
 
SUHU_MIN, SUHU_MAX = 15.0, 38.0
 
 
def baca_sensor(jumlah=None):
    n = 0
    while jumlah is None or n < jumlah:
        yield round(random.uniform(SUHU_MIN, SUHU_MAX), 1)
        n += 1
 
 
def kategori_suhu(suhu):
    if suhu < 20:
        return "Dingin"
    if suhu <= 30:
        return "Normal"
    return "Panas"
 
 
def stream_berstatus(sumber):
    for suhu in sumber:
        yield suhu, kategori_suhu(suhu)
 
 
def main():
    random.seed(42) 
 
    print("=== A. Konsumsi manual dengan next() ===")
    sensor = baca_sensor()
    for i in range(1, 4):
        suhu = next(sensor)
        print(f"next() ke-{i}: {suhu:.1f} C -> {kategori_suhu(suhu)}")
 
    print("\n=== B. Streaming 12 pembacaan berturut-turut ===")
    print(f"{'No':<4}{'Suhu (C)':>10}   Status")
    print("-" * 28)
    # islice mengambil 12 data pertama tanpa membuat list
    for no, (suhu, status) in enumerate(islice(stream_berstatus(baca_sensor()), 12), 1):
        print(f"{no:<4}{suhu:>10.1f}   {status}")
 
    print("\n=== C. Bukti efisiensi memori (1.000.000 data) ===")
    sebagai_list = [round(random.uniform(SUHU_MIN, SUHU_MAX), 1) for _ in range(1_000_000)]
    sebagai_generator = baca_sensor(1_000_000)
    print(f"List      : {sys.getsizeof(sebagai_list):>10,} byte (belum termasuk isi float-nya)")
    print(f"Generator : {sys.getsizeof(sebagai_generator):>10,} byte")
 
 
if __name__ == "__main__":
    main()