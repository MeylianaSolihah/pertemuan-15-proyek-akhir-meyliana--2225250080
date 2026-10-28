# Proposal Proyek Akhir Alpro 15

## 1. Judul
Program Rekap dan Analisis Nilai Matematika Kelas

## 2. Latar Belakang
Pengolahan nilai siswa perlu dilakukan secara teliti agar guru dapat mengetahui hasil belajar siswa. Program ini dibuat untuk membantu proses rekapitulasi dan analisis nilai secara sederhana menggunakan Python.

## 3. Tujuan
- Membaca data nilai siswa dari file teks.
- Memvalidasi data nama dan nilai.
- Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
- Menentukan jumlah siswa yang tuntas dan belum tuntas berdasarkan KKM.
- Menyimpan hasil analisis ke dalam file laporan.

## 4. Deskripsi Program
Program membaca data siswa dengan format nama dan nilai yang dipisahkan koma. Data yang tidak sesuai format atau memiliki nilai di luar rentang 0 sampai 100 akan dilewati. Data yang valid kemudian dianalisis dan hasilnya ditampilkan di terminal serta disimpan dalam file laporan.

## 5. Struktur Data dan Algoritma
Data siswa disimpan dalam list yang berisi dictionary dengan kunci nama dan nilai. Program menggunakan perulangan untuk membaca data, percabangan untuk validasi, serta fungsi untuk menghitung statistik nilai.

## 6. Pembagian Modul
- `main.py`: menjalankan alur utama program.
- `data_io.py`: membaca dan memvalidasi data.
- `analisis.py`: menghitung statistik dan ketuntasan.
- `utilitas.py`: menampilkan dan menyimpan laporan.

## 7. Pengujian
Pengujian dilakukan menggunakan modul unittest Python, meliputi data normal, nilai batas bawah dan atas, data tidak valid, file tidak ditemukan, nilai sama dengan KKM, serta data kosong.

## 8. Hasil yang Diharapkan
Program dapat mengolah data nilai yang valid, menampilkan statistik dengan benar, memberikan peringatan untuk data tidak valid, dan menyimpan laporan hasil analisis.

## 9. Batasan
- Data masukan menggunakan file teks.
- Nilai siswa berada pada rentang 0 sampai 100.
- KKM ditetapkan sebesar 75.
- Program dijalankan melalui terminal Python.

## 10. Referensi dan Bantuan
Dokumentasi Python: https://docs.python.org/3/

Bantuan AI digunakan sebagai pendamping dalam penyusunan kode dan dokumentasi. Program dijalankan dan diuji kembali untuk memeriksa fungsinya.
