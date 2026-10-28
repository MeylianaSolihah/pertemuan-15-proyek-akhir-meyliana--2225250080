from pathlib import Path


def baca_data_nilai(nama_file="data/nilai_contoh.txt"):
    """Membaca dan memvalidasi data nilai siswa."""
    path = Path(nama_file)
    if not path.is_file():
        print(f"File tidak ditemukan: {nama_file}")
        return []

    data = []
    with path.open("r", encoding="utf-8-sig") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()
            if not baris:
                continue
            bagian = baris.split(",")
            if len(bagian) != 2 or not bagian[0].strip():
                print(f"Format atau nama tidak valid pada baris {nomor}.")
                continue
            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                print(f"Nilai bukan angka pada baris {nomor}.")
                continue
            if not 0 <= nilai <= 100:
                print(f"Nilai harus 0-100 pada baris {nomor}.")
                continue
            data.append({"nama": bagian[0].strip(), "nilai": nilai})
    return data
