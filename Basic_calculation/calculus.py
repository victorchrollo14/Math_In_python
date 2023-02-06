import sympy as smp
from sympy import *
import re

# ♾️ == oo;  square_root = sqrt(val); exponential = exp(val)


class Calculus:

    def __init__(self, expr, wrt_var):
        self.expr = expr
        self.wrt_var = wrt_var

    def indefinate(self):
        ans = integrate(self.expr, self.wrt_var)
        pprint(ans)

    def definate(self, l_limit, U_limit):
        ans = integrate(self.expr, (self.wrt_var, l_limit, U_limit))
        pprint(ans)

    def derivative(self):
        ans = diff(self.expr, self.wrt_var)
        pprint(ans)

    def double_integration(self, *args):
        ans = integrate(
            self.expr, (self.wrt_var, args[0], args[1]), (args[2], args[3], args[4]))
        pprint(ans)

    def triple_integration(self, *args):
        ans = integrate(self.expr, (self.wrt_var, args[0], args[1]), (
            args[2], args[3], args[4]), (args[5], args[6], args[7]))
        pprint(ans)

    def limits(self, tends_to_val):
        ans = Limit(self.expr, self.wrt_var, tends_to_val)
        pprint(ans.doit())


def with_respect_to():
    wrt_var = input("enter the with respect to variable:(x or y or z)\n")
    return symbols(f"{wrt_var}")


def lower_upper_limit():
    lower_limit = input('enter the lower limit:')
    upper_limit = input('enter the upper limit:')
    return lower_limit, upper_limit


# x, y, z, a, b = smp.symbols('x y z a b')
init_printing(use_unicode=True)

operation_name = {

    1: 'indefinate integration',
    2: 'definate intergration',
    3: 'differentiation',
    4: 'double integration',
    5: 'triple integration',
    6: 'gamma value',
    7: 'limits'

}

for opt in operation_name:
    print(opt, operation_name[opt])

option = int(input(f"\nenter the operation number:"))
expr = input("\nenter the expression/question: ")
pprint(simplify(expr))

if (option == 1):
    wrt_var = with_respect_to()
    obj1 = Calculus(expr, wrt_var)
    obj1.indefinate()

if (option == 2):
    wrt_var = with_respect_to()
    lower_limit, upper_limit = lower_upper_limit()
    obj2 = Calculus(expr, wrt_var)
    obj2.definate(lower_limit, upper_limit)

if (option == 3):
    wrt_var = with_respect_to()
    obj3 = Calculus(expr, wrt_var)
    obj3.derivative()

if (option == 4):
    wrt_var = with_respect_to()
    lower_limit, upper_limit = lower_upper_limit()

    wrt_var1 = with_respect_to()
    lower_lim1, upper_lim1 = lower_upper_limit()

    obj4 = Calculus(expr, wrt_var)
    obj4.double_integration(lower_limit, upper_limit,
                            wrt_var1, lower_lim1, upper_lim1)

if (option == 5):
    wrt_var = with_respect_to()
    lower_limit, upper_limit = lower_upper_limit()

    wrt_var1 = with_respect_to()
    lower_lim1, upper_lim1 = lower_upper_limit()

    wrt_var2 = with_respect_to()
    lower_lim2, upper_lim2 = lower_upper_limit()

    obj5 = Calculus(expr, wrt_var)
    obj5.triple_integration(lower_limit, upper_limit, wrt_var1,
                            lower_lim1, upper_lim1, wrt_var2, lower_lim2, upper_lim2)

# if (option == 6):
#     m = int(input('enter the m value: '))
#     n = int(input("enter n value: "))
#     beta_val = gamma(m)*gamma(n)/gamma(m+n)
#     print(f"Beta(m,n): {beta_val}")

if (option == 7):
    """  
       To calculate limit:
         smp.limit(expr, wrt_var, tends_to, dir = '+')  
         for lim   (expr)
             x -> 0+
    """
    tends_to = input('enter the tends to variable: ')
    tends_to_val = input('enter the tends to value: ')
    tends_to = symbols(f'{tends_to}')

    obj6 = Calculus(expr, tends_to)
    obj6.limits(tends_to_val)
