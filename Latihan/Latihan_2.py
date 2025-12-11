"""
Latihan 2: Validasi Daftar Nilai Mahasiswa
Program untuk menghitung rata-rata nilai dengan penanganan data tidak valid
"""

def hitung_rata_rata_nilai():
    """
    Fungsi untuk menghitung rata-rata nilai mahasiswa
    dengan menangani data yang bukan angka
    """
    # Data nilai mahasiswa (ada yang berupa string)
    nilai = [80, 90, 'A', 70, 100, 'B']

    print("=" * 60)
    print("PROGRAM VALIDASI DAFTAR NILAI MAHASISWA")
    print("=" * 60)
    print(f"\nData nilai: {nilai}")
    print("\nMemproses data...")
    print("-" * 60)

    # Variabel untuk menyimpan hasil
    total_nilai = 0
    jumlah_valid = 0
    data_tidak_valid = []

    # Looping setiap elemen dalam list
    for i, n in enumerate(nilai):
        try:
            # Coba konversi ke float dan tambahkan ke total
            nilai_angka = float(n)
            total_nilai += nilai_angka
            jumlah_valid += 1

            print(f"Index {i}: {n} ✓ (Valid)")

        except ValueError:
            # Jika data bukan angka, skip dan catat
            print(f"Index {i}: {n} ✗ (Tidak valid. bukan angka, akan dilewati)")
            data_tidak_valid.append(n)

        except Exception as e:
            # Tangkap error lain yang tidak terduga
            print(f"Index {i}: Error tidak terduga - {e}")

    # Hitung rata-rata
    print("-" * 60)

    if jumlah_valid > 0:
        rata_rata = total_nilai / jumlah_valid

        print(f"\n HASIL PERHITUNGAN:")
        print(f"   Total nilai valid    : {total_nilai}")
        print(f"   Jumlah data valid    : {jumlah_valid}")
        print(f"   Data tidak valid     : {data_tidak_valid}")
        print(f"   Rata-rata nilai      : {rata_rata:.2f}")
    else:
        print("\n  Tidak ada data valid untuk dihitung!")

    print("=" * 60)

# Jalankan program
if __name__ == "__main__":
    hitung_rata_rata_nilai()

    # Bonus: Coba dengan data lain
    print("\n" + "=" * 60)
    print("Coba dengan data custom")
    print("=" * 60)

    try:
        # Input data sendiri (opsional)
        input_user = input("\nMau coba input nilai sendiri? (y/n): ").lower()

        if input_user == 'y':
            print("\nMasukkan nilai-nilai dipisahkan koma")
            print("Contoh: 80, 90, A, 70, B, 100")

            data_input = input("Input: ")
            # Split berdasarkan koma
            nilai_custom = [item.strip() for item in data_input.split(',')]

            print(f"\nData yang diinput: {nilai_custom}")
            print("\nMemproses...")

            # Proses data custom
            total = 0
            valid = 0

            for item in nilai_custom:
                try:
                    angka = float(item)
                    total += angka
                    valid += 1
                    print(f"  {item} ✓")
                except ValueError:
                    print(f"  {item} ✗ (dilewati)")

            if valid > 0:
                print(f"\nRata-rata: {total/valid:.2f}")
            else:
                print("\nTidak ada data valid!")

    except Exception as e:
        print(f"Terjadi error: {e}")


