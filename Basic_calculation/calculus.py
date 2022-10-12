# calculator 
import sympy as smp
from sympy import *
import re

class Calculus:
    def __init__(self,expr,wrt_var):
        self.expr = expr
        self.wrt_var = wrt_var

    def indefinate(self):
        print(integrate(self.expr,self.wrt_var))

    def definate(self,l_limit, U_limit):
        print(integrate(self.expr,(self.wrt_var,l_limit,U_limit)))





x,y = smp.symbols('x y')
init_printing(use_unicode=True)
expr = input("enter the expression in x and y terms:")
opt = input("enter the operation:definate integration,indefinate integration,differentiation,etc:\n")

if(re.search('^indefinate',opt,re.IGNORECASE)):
    wrt_var = input("enter the with respect to variable:(eg x or y or z)\n")
    wrt_var = symbols('x') if(wrt_var == 'x') else  symbols('y')
    obj1 = Calculus(expr,wrt_var)
    obj1.indefinate()

if(re.search('^definate',opt)):
    wrt_var = input("enter the with respect to variable:(x or y or z)\n")
    wrt_var = symbols('x') if(wrt_var == 'x') else symbols('y')
    lowerLimit = input("enter the lower limit of Integral:")
    upperLimit = input("enter the upper limit of Integral:")
    obj2 = Calculus(expr,wrt_var)
    obj2.definate(lowerLimit,upperLimit)
    


