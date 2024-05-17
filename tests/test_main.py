import unittest
from PIL import Image
from src.main import po2, po2_add

class TestGameImageResizer(unittest.TestCase):

    def test_po2(self):
        im = Image.new('RGB', (500, 300))
        resized_im = po2(im)
        self.assertEqual(resized_im.size, (512, 512))

    def test_po2_add(self):
        im = Image.new('RGB', (500, 300))
        resized_im = po2_add(im)
        self.assertEqual(resized_im.size, (512, 512))
        self.assertEqual(resized_im.crop((6, 106, 506, 406)).tobytes(), im.tobytes())

if __name__ == '__main__':
    unittest.main()
