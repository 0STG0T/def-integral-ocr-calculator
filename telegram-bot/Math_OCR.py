from pix2tex import cli as pix2tex
from PIL import Image

class OCR:
    def __init__(self):
        self.model = pix2tex.LatexOCR()
        
    def predict(self, path_to_img):
        img = Image.open(path_to_img)
        ltx = self.model(img=img)
        
        return ltx