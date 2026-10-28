# Panduan Penggunaan Program

## 1. Menyiapkan Data
Buka file `data/nilai_contoh.txt`. Setiap baris berisi nama dan nilai yang dipisahkan koma.

## 2. Menjalankan Program
Jalankan dari direktori utama proyek:

    python src/main.py

## 3. Melihat Hasil
Program menampilkan nilai setiap siswa, status ketuntasan, rata-rata, nilai tertinggi, nilai terendah, dan jumlah siswa tuntas.

## 4. Melihat Laporan
Jika terdapat data valid, laporan disimpan di `output/laporan_nilai.txt`.

## 5. Menjalankan Pengujian
Jalankan:

    python -m unittest discover -s tests -v
