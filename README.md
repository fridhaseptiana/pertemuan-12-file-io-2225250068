# Pertemuan 12 - File I/O dan Error Handling

**Nama:** Fridha Septiana  
**NIM:** 2225250068  
**Kelas:** 3E

## Tujuan

Membaca, memvalidasi, mengolah, dan menulis data file menggunakan Python serta menangani kesalahan yang mungkin terjadi saat pemrosesan file dan konversi tipe data.

## Format File Input

File input disimpan di `data/nilai.txt` dengan format:

```text
NIM,nilai
```

Contoh:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Setiap baris berisi NIM dan nilai yang dipisahkan dengan tanda koma. Baris kosong dilewati, sedangkan nilai yang tidak dapat dikonversi menjadi angka akan dilaporkan dan dilewati.

## Cara Menjalankan

Jalankan program melalui Terminal VS Code dengan perintah:

```bash
python3 tugas/rekap_nilai_file.py
```

Program membaca data dari `data/nilai.txt`, menghitung jumlah data valid, rata-rata, nilai minimum, nilai maksimum, dan jumlah mahasiswa yang lulus dengan nilai minimal 60. Hasil rekap disimpan dalam `data/hasil_rekap.txt`.

## Error yang Ditangani

1. **FileNotFoundError**  
   Ditangani ketika file input tidak ditemukan. Program menampilkan pesan yang jelas dan tidak berhenti akibat error tersebut.

2. **ValueError**  
   Ditangani ketika nilai tidak dapat dikonversi menjadi angka atau format baris tidak sesuai. Baris yang tidak valid dilewati sehingga data lainnya tetap diproses.

3. **OSError**  
   Ditangani ketika terjadi kesalahan saat menulis file hasil rekap.

## Test Case

**1. Kondisi normal**

- Kondisi: File input berisi data nilai yang valid.
- Hasil yang diharapkan: Data diproses dan statistik dihitung dengan benar.
- Hasil aktual: Data valid berhasil diproses dan hasil rekap disimpan.
- Status: Berhasil.

**2. File tidak ditemukan**

- Kondisi: File `data/nilai.txt` tidak tersedia.
- Hasil yang diharapkan: Program menampilkan pesan file tidak ditemukan tanpa crash.
- Hasil aktual: Program menampilkan pesan file tidak ditemukan.
- Status: Berhasil.

**3. Nilai tidak valid**

- Kondisi: Terdapat baris `A004,abc`.
- Hasil yang diharapkan: Baris invalid dilewati dan data lainnya tetap diproses.
- Hasil aktual: Baris invalid dilaporkan dan data valid lainnya tetap diproses.
- Status: Berhasil.

**4. Baris kosong**

- Kondisi: File input mengandung baris kosong.
- Hasil yang diharapkan: Baris kosong dilewati.
- Hasil aktual: Baris kosong dilewati tanpa menghentikan program.
- Status: Berhasil.

**5. Batas kelulusan**

- Kondisi: Terdapat data dengan nilai 60.
- Hasil yang diharapkan: Nilai 60 dihitung sebagai lulus.
- Hasil aktual: Nilai 60 termasuk dalam jumlah mahasiswa yang lulus.
- Status: Berhasil.

## Refleksi

Pada latihan ini, saya mempelajari cara membaca data dari file, memvalidasi setiap baris, menghitung statistik, dan menyimpan hasil rekap ke file baru. Salah satu error yang ditemukan adalah `ValueError` ketika nilai berupa teks, seperti `abc`, tidak dapat dikonversi menjadi angka. Error tersebut ditangani menggunakan `try-except` sehingga baris yang tidak valid dapat dilewati tanpa menghentikan seluruh proses. Dengan demikian, program dapat tetap mengolah data valid dan menghasilkan rekap nilai.
