"""
Latihan 1: Kalkulator Aman
Program kalkulator sederhana dengan penanganan eksepsi
"""


def kalkulator_aman():
    """
    Fungsi kalkulator yang menangani berbagai jenis error
    """
    print("=" * 50)
    print("KALKULATOR AMAN")
    print("=" * 50)

    try:
        # Input angka pertama
        angka1 = float(input("Masukkan angka pertama: "))

        # Input angka kedua
        angka2 = float(input("Masukkan angka kedua: "))

        # Input operator
        operator = input("Masukkan operator (+, -, *, /): ")

        # Validasi operator
        operator_valid = ['+', '-', '*', '/']
        if operator not in operator_valid:
            raise Exception(f"Operator '{operator}' tidak valid! Gunakan +, -, *, atau /")

        # Proses perhitungan
        if operator == '+':
            hasil = angka1 + angka2
        elif operator == '-':
            hasil = angka1 - angka2
        elif operator == '*':
            hasil = angka1 * angka2
        elif operator == '/':
            # Pengecekan pembagian dengan nol
            if angka2 == 0:
                raise ZeroDivisionError("Tidak bisa membagi dengan nol!")
            hasil = angka1 / angka2

        # Tampilkan hasil
        print(f"\nHasil: {angka1} {operator} {angka2} = {hasil}")

    except ValueError:
        print("\nError: Input harus berupa angka, bukan huruf!")
        print("Contoh yang benar: 10, 5.5, -3")

    except ZeroDivisionError as e:
        print(f"\nError Pembagian: {e}")
        print("Pembagi tidak boleh nol!")

    except Exception as e:
        print(f"\nError: {e}")

    finally:
        print("\n" + "=" * 50)
        print("Terima kasih telah menggunakan kalkulator!")
        print("=" * 50)


# Jalankan program
if __name__ == "__main__":
    # Loop agar bisa hitung berkali-kali
    while True:
        kalkulator_aman()

        ulangi = input("\nMau hitung lagi? (y/n): ").lower()
        if ulangi != 'y':
            print("\nSampai jumpa!")
            break