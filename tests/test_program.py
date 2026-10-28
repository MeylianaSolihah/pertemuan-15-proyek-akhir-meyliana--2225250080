import tempfile
import unittest
from pathlib import Path

from src.data_io import baca_data_nilai
from src.analisis import analisis_nilai


class TestProgramNilai(unittest.TestCase):

    def buat_file(self, isi):
        file = tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", delete=False
        )
        file.write(isi)
        file.close()
        self.addCleanup(Path(file.name).unlink, missing_ok=True)
        return file.name

    def test_rata_rata_data_normal(self):
        data = [
            {"nama": "Ani", "nilai": 80},
            {"nama": "Budi", "nilai": 70},
            {"nama": "Citra", "nilai": 90},
        ]
        hasil = analisis_nilai(data)
        self.assertEqual(hasil["rata_rata"], 80)

    def test_nilai_batas_bawah(self):
        file = self.buat_file("Ani,0\n")
        self.assertEqual(baca_data_nilai(file)[0]["nilai"], 0)

    def test_nilai_batas_atas(self):
        file = self.buat_file("Ani,100\n")
        self.assertEqual(baca_data_nilai(file)[0]["nilai"], 100)

    def test_nilai_tidak_valid_diabaikan(self):
        file = self.buat_file("Ani,105\nBudi,abc\nCitra,80\n")
        data = baca_data_nilai(file)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["nama"], "Citra")

    def test_file_tidak_ditemukan(self):
        self.assertEqual(
            baca_data_nilai("file_yang_tidak_ada_12345.txt"), []
        )

    def test_kkm_75_dinyatakan_tuntas(self):
        hasil = analisis_nilai([{"nama": "Ani", "nilai": 75}])
        self.assertEqual(hasil["jumlah_lulus"], 1)

    def test_data_kosong(self):
        hasil = analisis_nilai([])
        self.assertIsNone(hasil["rata_rata"])


if __name__ == "__main__":
    unittest.main()
