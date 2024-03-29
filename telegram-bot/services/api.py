import os

from services.Integrator import IntegralCalculator
from services.Math_OCR import OCR
from PIL import Image

import matplotlib.pyplot as plt

import os

import os


class API:
    def __init__(self) -> None:
        self.ocr_model = OCR()

    def get_latex(self, img: Image) -> str:
        """
        Args:
            img (PIL.Image): Image with an integral
        Returns:
            str: Integral in LaTex format
        """
        ltx = self.ocr_model.predict(img=img)
        return ltx


    def plot_latex(ltx: str, out_path: str, id: str) -> None:
        """
        Args:
            ltx (str): LaTex string
            out_path (str): Path where the picture of the plot will be saved
            id (str): Unique identifier
        """

        # Generate the image
        a = rf'{ltx}'
        ax = plt.axes([0, 0, 0.3, 0.3])  # left,bottom,width,height
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        plt.text(0.4, 0.4, '$%s$' % a, size=50, color="green")
        
        try:
            os.mkdir(path=out_path)
        except:
            pass
        
        file_path = f'latex_integral_{id}.png'

        try:
            # Check if the file already exists
            if os.path.exists(file_path):
                raise FileExistsError(f"'{file_path}' already exists")
        except:
            pass
        # Save the image
        plt.savefig(file_path)

    def integrate_from_latex(ltx: str, n_chunks: int) -> dict:
        """
        Args:
            ltx (str): LaTex string.
            n_chunks (int): How many times the function will be divided into chunks.
        """

        ltx = ltx[ltx.find('\int'):]
        calc = IntegralCalculator(ltx)

        try:
            answer_dict = {}

            # success flag
            answer_dict['success'] = True

            answer_dict['n_chunks'] = n_chunks
            answer_dict['squares_method'] = calc.integrate_by_squares(n_chunks)
            answer_dict['trapezoids_method'] = calc.integrate_by_trapezoids(n_chunks)
            answer_dict['parabolic_method'] = calc.integrate_by_parabolic(n_chunks)

            return answer_dict

        except:
            return {'success': False}
