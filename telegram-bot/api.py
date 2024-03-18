from Integrator import IntegralCalculator
from Math_OCR import OCR
from PIL import Image

class API:
    def __init__(self) -> None:
        self.ocr_model = OCR()
        
    def get_latex(self, img: Image) -> str:
        """
        Args: path_to_img (PIL.Image): image with an integral
        Returns: (str) Integral in LaTex format
        """

        ltx = self.ocr_model.predict(img=img)
        
        return ltx
    
    def plot_latex(ltx: str, out_path: str) -> None:
        """
        Args:
            ltx (str): LaTex string
            out_path (str): path where the picture of the plot will be saved
        """
        
        import matplotlib.pyplot as plt

        a = rf'{ltx}'
        ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('off')
        plt.text(0.4,0.4,'$%s$' %a,size=50,color="green")
        
        plt.savefig(out_path + '/' + 'latex_integral.jpg')
        
    def integrate_from_latex(ltx: str, n_chunks: int) -> dict:
        """
        Args:
            ltx (str): LaTex string.
            n_chunks (int): How many times the function will be divided into chunks.
        """
        
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
        