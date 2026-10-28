# Dokumentasi Pengujian Program

| No. | Skenario Pengujian | Hasil yang Diharapkan | Status |
|---|---|---|---|
| 1 | Data nilai normal | Rata-rata dihitung dengan benar | Berhasil |
| 2 | Nilai 0 | Nilai diterima | Berhasil |
| 3 | Nilai 100 | Nilai diterima | Berhasil |
| 4 | Nilai di luar rentang 0–100 | Data tidak valid diabaikan | Berhasil |
| 5 | File tidak ditemukan | Program menampilkan pesan dan mengembalikan data kosong | Berhasil |
| 6 | Nilai sama dengan KKM 75 | Siswa dinyatakan tuntas | Berhasil |
| 7 | Data kosong | Rata-rata bernilai kosong | Berhasil |

Pengujian otomatis dilakukan menggunakan modul unittest Python.
