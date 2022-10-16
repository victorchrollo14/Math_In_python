import sympy as sym
from sympy import *
import numpy as np

from .num_util import finding_roots, falsi_formula, temp_roots

class NumericalMethods():
    def __init__(self,expr):
        self.expr = expr
        
    def regular_falsi():
        pass



    

x = symbols('x')
# expr = input("enter the expression: ")
expr = x**3 - 2*x - 5
expr = simplify(expr)
pprint(expr)

m, n = finding_roots(expr)
print(f'The roots are ({m},{n})')

sec_roots = temp_roots(expr, m, n)
print(f"The new roots are: {sec_roots}")

root_values = falsi_formula(expr, m, n)




