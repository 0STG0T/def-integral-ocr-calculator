from pix2tex import cli as pix2tex
from PIL import Image


class OCR:
    def __init__(self):
        self.model = pix2tex.LatexOCR()

    def predict(self, img: Image):
        ltx = self.model(img=img)

        return ltx
