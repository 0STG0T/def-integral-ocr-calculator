from latex2sympy2 import latex2sympy
import sympy as sp


class IntegralCalculator:
    def __init__(self, integral_str):

        self.lower_limit, self.upper_limit, self.function = self._parse_integral_input(integral_str)
        x = sp.symbols('x')
        self.function_lambda = sp.lambdify(x, self.function, 'numpy')
        self.x = x

    def _parse_integral_input(self, integral_str):
        # Convert LaTeX to sympy expression
        integral_expr = latex2sympy(integral_str, {"integrate": False})

        lower_limit = integral_expr.limits[0][1]
        upper_limit = integral_expr.limits[0][2]
        function = integral_expr.function

        return float(lower_limit), float(upper_limit), function

    def integrate_by_squares(self, n):
        h = (self.upper_limit - self.lower_limit) / n
        result = 0
        for i in range(n):
            midpoint = self.lower_limit + (i + 0.5) * h
            result += self.function_lambda(midpoint)
        return result * h

    def integrate_by_trapezoids(self, n):
        h = (self.upper_limit - self.lower_limit) / n
        result = (self.function_lambda(self.lower_limit) + self.function_lambda(self.upper_limit)) / 2
        for i in range(1, n):
            result += self.function_lambda(self.lower_limit + i * h)
        return result * h

    def integrate_by_parabolic(self, n):
        if n % 2 == 1:
            n += 1
        h = (self.upper_limit - self.lower_limit) / n
        result = self.function_lambda(self.lower_limit) + self.function_lambda(self.upper_limit)
        for i in range(1, n):
            factor = 4 if i % 2 == 1 else 2
            result += factor * self.function_lambda(self.lower_limit + i * h)
        return result * h / 3
