import sympy as smp
from sympy import *
import re


class Calculus:
    def __init__(self, expr, wrt_var):
        self.expr = expr
        self.wrt_var = wrt_var

    def indefinate(self):
        print(integrate(self.expr, self.wrt_var))

    def definate(self, l_limit, U_limit):
        print(integrate(self.expr, (self.wrt_var, l_limit, U_limit)))

    def derivative(self):
        print(diff(self.expr, self.wrt_var))
    
    def partial_derivative(self):
        pass


def with_respect_to():
    wrt_var = input("enter the with respect to variable:(x or y or z)")
    return symbols(f"{wrt_var}")


x, y, z = smp.symbols('x y z')
print(f"Names of Operation:")
print(f'definate Integration\tIndefinate Integration\tdifferentiation\tPartial Differentiation\n')
expr = input("enter the expression in x and y terms:")
opt = input("enter the operation:definate integration,indefinate integration,differentiation,etc:\n")

if (re.search('^indefinate', opt, re.IGNORECASE)):
    wrt_var = with_respect_to()
    obj1 = Calculus(expr, wrt_var)
    obj1.indefinate()

if (re.search('^definate', opt, re.IGNORECASE)):
    wrt_var = with_respect_to()
    lowerLimit = input("enter the lower limit of Integral:")
    upperLimit = input("enter the upper limit of Integral:")
    obj2 = Calculus(expr, wrt_var)
    obj2.definate(lowerLimit, upperLimit)
 
if (re.search("^diff", opt, re.IGNORECASE)):
    wrt_var = with_respect_to()
    obj3 = Calculus(expr, wrt_var)
    obj3.derivative()
