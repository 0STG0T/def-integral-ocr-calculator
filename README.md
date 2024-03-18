# Pipeline of Definite Integral Optical Recognition + calculating it using squares, trapezoids and parabolas methods.
## It uses pix2tex library for OCR (image translates to latex string), latex2sympy2 (translates latex to sympy), sympy (integral calculation part).
### It struggles with handwrited expressions, but nails easy integrals like this: ![Simple Definite Integral](https://github.com/0STG0T/def-integral-ocr-calculator/blob/main/images/Screenshot%202024-03-18%20at%2013.37.54.png?raw=true)
### Reult of OCR: \int_{-2}^{3}(x^{2}-3)\,d x
### Result of calculation: 
####Количество разбийений: 1000
####Интегрирование методом средних квадратов: -3.3333437500000014
####Интегрирование методом трапеций: -3.333312499999998
####Интегрирование методом Симпсона (парабол): -3.3333333333333326
