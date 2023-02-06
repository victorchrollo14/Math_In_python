from sympy import *
from sympy import fourier_series, pi

from util.utils import with_respect_to as wrt, lower_upper_limit as upl


class FourierSeries:
    def __init__(self, expr):
        self.expr = expr

    def Fourier_Radian(self, *args):
        print(args[0], args[1], args[2])
        s = fourier_series(self.expr, (args[0], args[1], args[2]))
        soln = s.truncate(n=6)
        return soln

    def arbitary():
        pass

    def half_range_sine():
        pass

    def half_range_cosine():
        pass

    def series_expansion():
        pass


expr = input("Enter the expression: ")
expr = simplify(expr)
pprint(expr)

wrt_var = wrt()
llimit, ulimit = upl()

obj1 = FourierSeries(expr)
solution = obj1.Fourier_Radian(wrt_var, llimit, ulimit)
pprint(solution)
