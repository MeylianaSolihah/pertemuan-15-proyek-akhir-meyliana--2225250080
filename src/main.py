from data_io import baca_data_nilai
from analisis import analisis_nilai
from utilitas import tampilkan_laporan, simpan_laporan


def main():
    kkm = 75
    data = baca_data_nilai()
    hasil = analisis_nilai(data, kkm)
    tampilkan_laporan(data, hasil, kkm)
    if data:
        simpan_laporan(data, hasil, kkm)


if __name__ == "__main__":
    main()
