import tempfile
import unittest
from pathlib import Path

from src.data_io import baca_data_nilai


class TestValidasiData(unittest.TestCase):
    def test_format_dan_nilai_tidak_valid_diabaikan(self):
        isi = " ,80\nBudi,abc\nCitra,101\nDedi,75\n"

        with tempfile.TemporaryDirectory() as folder:
            file_data = Path(folder) / "data.txt"
            file_data.write_text(isi, encoding="utf-8")

            data = baca_data_nilai(str(file_data))

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["nama"], "Dedi")
        self.assertEqual(data[0]["nilai"], 75)


if __name__ == "__main__":
    unittest.main()
