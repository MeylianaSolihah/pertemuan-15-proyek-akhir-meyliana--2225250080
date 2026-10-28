from pathlib import Path


def tampilkan_laporan(data_nilai, hasil, kkm=75):
    print("\n=== REKAP NILAI MATEMATIKA ===")
    print(f"KKM: {kkm}")
    for nomor, siswa in enumerate(data_nilai, 1):
        status = "Tuntas" if siswa["nilai"] >= kkm else "Belum tuntas"
        print(f"{nomor}. {siswa['nama']}: {siswa['nilai']:g} - {status}")

    if hasil["rata_rata"] is None:
        print("Tidak ada data valid untuk dianalisis.")
        return

    print(f"Rata-rata: {hasil['rata_rata']:.2f}")
    print(f"Nilai tertinggi: {hasil['nilai_tertinggi']:g}")
    print(f"Nilai terendah: {hasil['nilai_terendah']:g}")
    print(f"Jumlah tuntas: {hasil['jumlah_lulus']}")
    print(f"Jumlah belum tuntas: {hasil['jumlah_tidak_lulus']}")


def simpan_laporan(data_nilai, hasil, kkm=75,
                   nama_file="output/laporan_nilai.txt"):
    path = Path(nama_file)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            file.write("REKAP NILAI MATEMATIKA\n")
            file.write(f"KKM: {kkm}\n")
            for siswa in data_nilai:
                status = "Tuntas" if siswa["nilai"] >= kkm else "Belum tuntas"
                file.write(f"{siswa['nama']}: {siswa['nilai']:g} - {status}\n")
            if hasil["rata_rata"] is not None:
                file.write(f"Rata-rata: {hasil['rata_rata']:.2f}\n")
                file.write(f"Nilai tertinggi: {hasil['nilai_tertinggi']:g}\n")
                file.write(f"Nilai terendah: {hasil['nilai_terendah']:g}\n")
                file.write(f"Jumlah tuntas: {hasil['jumlah_lulus']}\n")
                file.write(f"Jumlah belum tuntas: {hasil['jumlah_tidak_lulus']}\n")
        print(f"Laporan disimpan: {path}")
        return True
    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
        return False
