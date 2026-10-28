def analisis_nilai(data_nilai, kkm=75):
    """Menghitung statistik nilai dan ketuntasan."""
    if not data_nilai:
        return {
            "rata_rata": None,
            "nilai_tertinggi": None,
            "nilai_terendah": None,
            "jumlah_lulus": 0,
            "jumlah_tidak_lulus": 0,
        }

    nilai = [siswa["nilai"] for siswa in data_nilai]
    jumlah_lulus = sum(n >= kkm for n in nilai)
    return {
        "rata_rata": sum(nilai) / len(nilai),
        "nilai_tertinggi": max(nilai),
        "nilai_terendah": min(nilai),
        "jumlah_lulus": jumlah_lulus,
        "jumlah_tidak_lulus": len(nilai) - jumlah_lulus,
    }
