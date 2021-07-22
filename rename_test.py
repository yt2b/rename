import unittest
import rename


class TestRename(unittest.TestCase):
    def test_read_exif(self):
        test_exif = {256: 1920, 36867: "2020:01:01 08:00:00"}
        test_patterns = [
            ("ImageWidth", 1920),
            ("DateTimeOriginal", "2020:01:01 08:00:00"),
            ("IvalidTag", None)
        ]
        for tag_name, expected in test_patterns:
            with self.subTest(tag_name=tag_name, expected=expected):
                actual = rename.read_exif(test_exif, tag_name)
                self.assertEqual(expected, actual)

    def test_convert_format(self):
        actual = rename.convert_format("2010:05:12 04:25:50", "%Y%m%d_%H%M%S")
        self.assertEqual("20100512_042550", actual)

    def test_rename_path(self):
        actual = rename.rename_path("/home/abc/before.txt", "after")
        self.assertEqual("/home/abc/after.txt", actual)
