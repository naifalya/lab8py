# Penangan Eksepsi

## Tujuan Praktikum
1. Memahami perbedaan antara syntax error dan runtime error
2. Menggunakan blok try-except untuk menangani error
3. Menangani berbagai jenis eksepsi spesifik (ValueError, ZeroDivisionError, dll)
4. Menggunakan klausa else dan finally
5. Membuat dan memicu eksepsi sendiri dengan raise

## Materi
**Exception (eksepsi)** adalah error yang terjadi saat program sedang berjalan (runtime). Berbeda dengan syntax error yang terdeteksi sebelum program dijalankan, exception terjadi ketika ada kondisi tidak normal saat eksekusi.

### Filosofi Python: EAFP vs LBYL
**EAFP (Easier to Ask for Forgiveness than Permission)**
- Coba dulu, kalau error baru tangani
- Menggunakan try-except
- Lebih "Pythonic"

**LBYL (Look Before You Leap)**
- Cek dulu sebelum eksekusi
- Menggunakan banyak if-else
- Kurang efisien

## Percobaan
1. _Percobaan ini menunjukkan pentingnya exception handling_
   
   Tujuan: melihat apa yang terjadi jika program tidak menangani error.
Program meminta dua angka lalu melakukan pembagian.
Jika pembagi = 0 → program berhenti dan muncul ZeroDivisionError. 

2. _Dasar penggunaan try–except_

   Dalam program yang sama ditambahkan blok try-except, sehingga jika user memasukkan 0, program tidak crash, melainkan menampilkan pesan sopan.

3. _Cara menangani beberapa error dalam satu blok._

   Menangani beberapa error sekaligus:
   - ValueError → user memasukkan huruf
   - ZeroDivisionError → pembagian dengan nol
   - Exception → penangkap umum untuk error lain
     
    Urutan penting: error paling spesifik harus ditulis dulu.

4. _Memahami alur lengkap exception flow_

     else dipakai untuk kode lanjutan yang hanya aman dijalankan jika input benar.
  finally cocok untuk cleanup atau pesan penutup.

5. _Cara membaca detail error untuk debugging._
   
    Program mencoba mengakses indeks list yang tidak ada.
    as e menampilkan pesan error asli dari Python (contoh: list index out of range).

6. _Teknik membuat validasi custom menggunakan raise._

    raise digunakan untuk memaksa munculnya error ketika kondisi tidak memenuhi aturan.
    Lalu error tersebut ditangkap oleh try–except.
   
## Latihan

### Latihan 1
Deskripsi Tugas
Membuat program kalkulator sederhana yang bisa menangani:

1. Input yang bukan angka (ValueError)
2. Pembagian dengan nol (ZeroDivisionError)
3. Operator tidak valid (custom Exception)

Analisis Permasalahan
Problem yang harus ditangani:

- User memasukkan huruf saat diminta angka → ValueError
- User membagi dengan 0 → ZeroDivisionError
- User memasukkan operator selain +, -, *, / → Custom Exception

Penjelasan Kode
1. Menangani ValueError
```
try:
    angka1 = float(input("Masukkan angka pertama: "))
except ValueError:
    print("Error: Input harus berupa angka!")
```

Penjelasan: Fungsi float() akan throw ValueError jika input bukan angka. Kita tangkap error ini agar program tidak crash.

2. Menangani ZeroDivisionError
```
if angka2 == 0:
    raise ZeroDivisionError("Tidak bisa membagi dengan nol!")
```
Penjelasan: Kita cek manual dan raise error sendiri dengan pesan yang lebih jelas.

3. Custom Exception untuk Operator
```
if operator not in operator_valid:
    raise Exception(f"Operator '{operator}' tidak valid!")
```
Penjelasan: Kita buat error sendiri menggunakan raise Exception() untuk kasus yang tidak ada exception bawaan Python-nya.

Dari latihan ini, mahasiswa memahami bahwa:
- Program harus tetap robust meskipun user salah input.
- Exception handling membuat program lebih aman dan nyaman digunakan.
- ValueError, ZeroDivisionError, dan custom Exception sangat penting pada validasi input.
- Pesan error custom membuat program lebih ramah bagi pengguna.
  
### Latihan 2

Deskripsi Tugas

Membuat program yang menghitung rata-rata nilai mahasiswa dari list yang berisi data campuran (angka dan string). Program harus:

1. Skip data yang bukan angka tanpa crash
2. Hitung rata-rata dari data valid saja
3. Lapor data mana yang tidak valid

Data yang diberikan:
```
nilai = [80, 90, 'A', 70, 100, 'B']
```
Problem:

Ada data string ('A', 'B') yang tidak bisa di-sum
Jika langsung dijumlahkan, program akan error
Butuh cara untuk skip data invalid tapi tetap proses yang valid

Solusi yang Diimplementasikan
Strategi:

1. Loop setiap elemen dalam list
2. Pakai try-except di dalam loop
3. Coba konversi ke float
4. Jika berhasil → tambahkan ke total
5. Jika gagal (ValueError) → skip dan catat
6. Hitung rata-rata dari data valid saja

Latihan ini mengajarkan bahwa:
- Exception handling bisa digunakan sebagai filter data, bukan hanya menangani error.
- Error pada satu elemen tidak perlu menghentikan seluruh proses.
- Sangat penting untuk memisahkan data valid & invalid saat mengolah data dunia nyata.
- try-except di dalam loop adalah teknik umum dalam pemrosesan data yang tidak bersih (dirty data).

## Kesimpulan
1. Exception Handling itu Penting=
   -Program yang bagus tidak boleh crash tiba-tiba
   -User experience lebih baik dengan error message yang jelas
   -Exception handling membuat program lebih robust


2. Try-Except Bukan untuk Semua Error
   -Syntax error tetap harus diperbaiki di kode
   -Try-except untuk runtime error yang unpredictable
   -Jangan pakai naked except (except:) tanpa tipe

3. Berbagai Cara Pakai Exception
   -Tangani error spesifik (ValueError, ZeroDivisionError)
   -Buat error sendiri dengan raise
   -Gunakan finally untuk cleanup
   -Try-except bisa di dalam loop


4. Best Practices yang Saya Terapkan
   -Pesan error yang informatif
   -Validasi input user
   -Logging/tracking error untuk debugging
   -Edge case handling (misal: pembagian dengan 0)
