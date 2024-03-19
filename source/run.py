from Integrator import IntegralCalculator
from Math_OCR import OCR

def main():
    path_to_img = input('Путь к изображению с интегралом:')
    n_chunks = int(input('Количество частей разбиения:'))

    ocr = OCR()
    
    ltx = ocr.predict(path_to_img=path_to_img)
    
    print('\n\n-------------- Результаты ---------------\n')
    print('Интеграл:', ltx)
    print('Количество разбийений:', n_chunks, '\n')
    
    calc = IntegralCalculator(ltx)
    
    print("Интегрирование методом средних квадратов:", calc.integrate_by_squares(n_chunks))
    print("Интегрирование методом трапеций:", calc.integrate_by_trapezoids(n_chunks))
    print("Интегрирование методом Симпсона (парабол):", calc.integrate_by_parabolic(n_chunks))
    print('\n\n--------------------------------------')
    

if __name__ == '__main__':
    main()