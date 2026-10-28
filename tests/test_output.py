import tempfile
import unittest
from pathlib import Path

from src.utilitas import simpan_laporan


class TestSimpanLaporan(unittest.TestCase):
    def test_laporan_berhasil_disimpan(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "laporan.txt"
            data = [{"nama": "Ani", "nilai": 80}]
            hasil = {
                "rata_rata": 80,
                "nilai_tertinggi": 80,
                "nilai_terendah": 80,
                "jumlah_lulus": 1,
                "jumlah_tidak_lulus": 0,
            }

            berhasil = simpan_laporan(
                data, hasil, nama_file=str(target)
            )

            self.assertTrue(berhasil)
            self.assertTrue(target.exists())
            self.assertIn(
                "Ani: 80 - Tuntas",
                target.read_text(encoding="utf-8"),
            )


if __name__ == "__main__":
    unittest.main()
